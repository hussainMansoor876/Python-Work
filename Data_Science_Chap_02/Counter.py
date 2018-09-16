from collections import Counter
document="New to Python or choosing between Python 2 and Python 3 ? Read Python 2 or Python 3"
word=Counter(document)
print(word)
print(Counter(document.split()))