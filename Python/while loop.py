num=1
even=[]
odd=[]
while num<=100:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
    num = num + 1
    #num+=1
print("Even numbers list:\n",even)
print("Odd numbers list:\n",odd)
print(sum(even))
print(sum(odd))
print(min(even))
print(max(even))
print(min(odd))
print(max(odd))
print(len(even))
print(len(odd))
print(list(even))