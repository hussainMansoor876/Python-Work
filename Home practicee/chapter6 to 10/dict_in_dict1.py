users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton','student':{"name":"Mansoor","Father name":"Manzoor Hussain","Class":"3rd year","age":19}
},'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
}}
print(users)
for key,value in users.items():
    print(key+":"+str(value))
    for key1,value1 in value.items():
        print(key1 + ":" + str(value1))
print(list(users.items()))