document="New to Python or choosing between Python 2 and Python 3 ? Read Python 2 or Python 3"
words={}
for word in document:
    if word in words:
        words[word]+=1
    else:
        words[word]=1
print(words)
print(len(document))
#print(sum(document))
#print(list(words))
document1=document.split()
words1={}
for word in document1:
    if word in words1:
        words1[word]+=1
    else:
        words1[word]=1
print(words1)
print(len(document1))
#print(sum(document))
