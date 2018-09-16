num=int(input("Enter number:"))
binary=[]
while num!=1:
    binary.append(num%2)
    num=num/2

#binary.append(num)
print(binary)