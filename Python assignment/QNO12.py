namesort=[]
for name1 in range(1,6):
    name1 = (str(input("Enter Name:")), int(input("Enter age:")), int(input("Enter height:")))
    print(name1)
    namesort.append(name1)
print(sorted(namesort))
#print(namesort)
#namesort.sort()
#print(namesort)