with open('text.py','w+') as fileObj:
    content=fileObj.write("I love u fabiha")
    print(content)
    fileObj.flush()
    fileObj.seek(0)
    content=fileObj.read()
    print(content)
