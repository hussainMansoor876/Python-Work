from random import randint
mylist=[]
for val in range(0,10):
    num = randint(1, 10)
    if (num in mylist):
        del num
    else:
        mylist.append(num)
print(mylist)