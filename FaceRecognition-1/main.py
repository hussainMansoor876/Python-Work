from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from tensorflow.python.platform import gfile
import numpy as np
import sys
import os
import detect_and_align
import id_data
from scipy import misc
import re
import cv2
import argparse
import time


def find_matching_id(id_dataset, embedding):
    threshold = 1.1
    min_dist = 10.0
    matching_id = None

    for id_data in id_dataset:
        dist = get_embedding_distance(id_data.embedding, embedding)

        if dist < threshold and dist < min_dist:
            min_dist = dist
            matching_id = id_data.name
    return matching_id, min_dist


def get_embedding_distance(emb1, emb2):
    dist = np.sqrt(np.sum(np.square(np.subtract(emb1, emb2))))
    return dist


def load_model(model):
    model_exp = os.path.expanduser(model)
    if (os.path.isfile(model_exp)):
        print('Model filename: %s' % model_exp)
        with gfile.FastGFile(model_exp, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            tf.import_graph_def(graph_def, name='')
    else:
        print('Model directory: %s' % model_exp)
        meta_file, ckpt_file = get_model_filenames(model_exp)

        print('Metagraph file: %s' % meta_file)
        print('Checkpoint file: %s' % ckpt_file)

        saver = tf.train.import_meta_graph(os.path.join(model_exp, meta_file))
        saver.restore(tf.get_default_session(), os.path.join(model_exp, ckpt_file))


def get_model_filenames(model_dir):
    files = os.listdir(model_dir)
    meta_files = [s for s in files if s.endswith('.meta')]
    if len(meta_files) == 0:
        raise ValueError('No meta file found in the model directory (%s)' % model_dir)
    elif len(meta_files) > 1:
        raise ValueError('There should not be more than one meta file in the model directory (%s)' % model_dir)
    meta_file = meta_files[0]
    meta_files = [s for s in files if '.ckpt' in s]
    max_step = -1
    for f in files:
        step_str = re.match(r'(^model-[\w\- ]+.ckpt-(\d+))', f)
        if step_str is not None and len(step_str.groups()) >= 2:
            step = int(step_str.groups()[1])
            if step > max_step:
                max_step = step
                ckpt_file = step_str.groups()[0]
    return meta_file, ckpt_file


def print_id_dataset_table(id_dataset):
    nrof_samples = len(id_dataset)

    print('Images:')
    for i in range(nrof_samples):
        print('%1d: %s' % (i, id_dataset[i].image_path))
    print('')

    print('Distance matrix')
    print('         ', end='')
    for i in range(nrof_samples):
        name = os.path.splitext(os.path.basename(id_dataset[i].name))[0]
        print('     %s   ' % name, end='')
    print('')
    for i in range(nrof_samples):
        name = os.path.splitext(os.path.basename(id_dataset[i].name))[0]
        print('%s       ' % name, end='')
        for j in range(nrof_samples):
            dist = get_embedding_distance(id_dataset[i].embedding, id_dataset[j].embedding)
            print('  %1.4f      ' % dist, end='')
        print('')


def test_run(pnet, rnet, onet, sess, images_placeholder, phase_train_placeholder, embeddings, id_dataset, test_folder):
    if test_folder is None:
        return

    image_names = os.listdir(os.path.expanduser(test_folder))
    image_paths = [os.path.join(test_folder, img) for img in image_names]
    nrof_images = len(image_names)
    aligned_images = []
    aligned_image_paths = []

    for i in range(nrof_images):
        image = misc.imread(image_paths[i])
        face_patches, _, _ = detect_and_align.align_image(image, pnet, rnet, onet)
        aligned_images = aligned_images + face_patches
        aligned_image_paths = aligned_image_paths + [image_paths[i]] * len(face_patches)

    aligned_images = np.stack(aligned_images)

    feed_dict = {images_placeholder: aligned_images, phase_train_placeholder: False}
    embs = sess.run(embeddings, feed_dict=feed_dict)

    for i in range(len(embs)):
        misc.imsave('outfile' + str(i) + '.jpg', aligned_images[i])
        matching_id, dist = find_matching_id(id_dataset, embs[i, :])
        if matching_id:
            print('Found match %s for %s! Distance: %1.4f' % (matching_id, aligned_image_paths[i], dist))
        else:
            print('Couldn\'t fint match for %s' % (aligned_image_paths[i]))


def main(args):
    with tf.Graph().as_default():
        with tf.Session() as sess:

            pnet, rnet, onet = detect_and_align.create_mtcnn(sess, None)

            load_model(args.model)
            images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
            embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
            phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")

            id_dataset = id_data.get_id_data(args.id_folder[0], pnet, rnet, onet, sess, embeddings, images_placeholder, phase_train_placeholder)
            print_id_dataset_table(id_dataset)

            test_run(pnet, rnet, onet, sess, images_placeholder, phase_train_placeholder, embeddings, id_dataset, args.test_folder)

            cap = cv2.VideoCapture(0)
            frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

            show_landmarks = False
            show_bb = False
            show_id = True
            show_fps = False
            while(True):
                start = time.time()
                _, frame = cap.read()

                face_patches, padded_bounding_boxes, landmarks = detect_and_align.align_image(frame, pnet, rnet, onet)

                if len(face_patches) > 0:
                    face_patches = np.stack(face_patches)
                    feed_dict = {images_placeholder: face_patches, phase_train_placeholder: False}
                    embs = sess.run(embeddings, feed_dict=feed_dict)

                    print('Matches in frame:')
                    for i in range(len(embs)):
                        bb = padded_bounding_boxes[i]

                        matching_id, dist = find_matching_id(id_dataset, embs[i, :])
                        if matching_id:
                            print('Hi %s! Distance: %1.4f' % (matching_id, dist))
                        else:
                            matching_id = 'Unkown'
                            print('Unkown! Couldn\'t fint match.')

                        if show_id:
                            font = cv2.FONT_HERSHEY_SIMPLEX
                            cv2.putText(frame, matching_id, (bb[0], bb[3]), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

                        if show_bb:
                            cv2.rectangle(frame, (bb[0], bb[1]), (bb[2], bb[3]), (255, 0, 0), 2)

                        if show_landmarks:
                            for j in range(5):
                                size = 1
                                top_left = (int(landmarks[i, j]) - size, int(landmarks[i, j + 5]) - size)
                                bottom_right = (int(landmarks[i, j]) + size, int(landmarks[i, j + 5]) + size)
                                cv2.rectangle(frame, top_left, bottom_right, (255, 0, 255), 2)
                else:
                    print('Couldn\'t find a face')

                end = time.time()

                seconds = end - start
                fps = round(1 / seconds, 2)

                if show_fps:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(frame, str(fps), (0, int(frame_height) - 5), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

                cv2.imshow('frame', frame)

                key = cv2.waitKey(1)
                if key == ord('q'):
                    break
                elif key == ord('l'):
                    show_landmarks = not show_landmarks
                elif key == ord('b'):
                    show_bb = not show_bb
                elif key == ord('i'):
                    show_id = not show_id
                elif key == ord('f'):
                    show_fps = not show_fps

            cap.release()
            cv2.destroyAllWindows()


def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('model', type=str, help='Could be either a directory containing the meta_file and ckpt_file or a model protobuf (.pb) file')
    parser.add_argument('id_folder', type=str, nargs='+', help='Folder containing ID folders')
    parser.add_argument('--test_folder', type=str, help='Folder containing test images.', default=None)
    return parser.parse_args(argv)

if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
