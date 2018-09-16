from collections import defaultdict
document="New to Python or choosing between Python 2 and Python 3 ? Read Python 2 or Python 3"
words=defaultdict(int)
for word in document:
    words[word]+=1
print(words)
words1=[]
'''for word in document.split():
    words1[word]+=1
print(words1)'''