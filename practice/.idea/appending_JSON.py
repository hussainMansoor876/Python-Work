import json
new_dictionary={'f_name':'Man'}
with open('test.json','a') as file:
    file.write(json.dumps(new_dictionary,indent=True))
with open('test.json') as file1:
    data=file1.readlines()
    for line in data:
        a=line
