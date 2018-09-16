document="New to Python or choosing between Python 2 and Python 3 ? Read Python 2 or Python 3"
words={}
for word in document:
    words[word]=words.get(word,0)+1
print(words)