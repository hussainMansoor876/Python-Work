document="New to Python or choosing between Python 2 and Python 3 ? Read Python 2 or Python 3"
words={}
for word in document:
    words[word]=words.get(word,0)+1
print(words)
word1={}
for count in document.split():
    word1[count]=word1.get(count,0)+1
print(word1)
for key,value in word1.items():
    print("key=",key,"value=",value)