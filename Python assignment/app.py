from collections import Counter
sentence="New to Python or choosing between Python 2 and Python 3 ? Read Python 2 or Python 3"
characters={}
words=sentence.split()
print(words)
# for word in sentence.split():
#     characters[word] = characters.get(word, 0) + 1
# print(characters)
# for key,value in characters.items():
#     print(key,",",value)
# word_counts = Counter(words)
# print(word_counts)