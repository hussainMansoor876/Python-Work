value=int(input("Enter number:"))
num=1
count=0
while num<=value:
    if(value%num==0):
        count+=1
    num+=1
if(count<=2):
    print("This is a prime number")
else:
    print("This is not a prime number")
