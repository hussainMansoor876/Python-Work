import json
name=[{'1 Client': {'name': 'mansoor', 'id': 888, 'address': '999', 'balance': 'Rs 999'}}]
with open('username.json','a') as file:
    file.write("\n"+str(name))
with open('username.json') as file:
    name=file.read()
    for name1 in name.split('\n'):
        if 'hussain' in name1:
            print(name1)

