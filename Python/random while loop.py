from random import randint
maximum=int(input("Enter maximum number"))
count=maximum+1
mylist=[]
while len(mylist)!=count:
    num=randint(0,maximum)
    if(num not in mylist):
        mylist.append(num)
print(mylist)
mylist.sort()
print("After sorting the number")
print(mylist)