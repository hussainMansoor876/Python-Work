allien={'color':'green','points':5,'age':'7 years',4:'mansoor'}
#print(allien['color'])
#print(allien['points'])
#print(allien['age'])
#print(allien[4])
for key,value in allien.items():
    print("\nkey:",key,"value:",value)

print(allien.items())
for val in allien.keys():
    print("Key:",val)
for val2 in allien.values():
    print("values:",val2)
