from collections import defaultdict
import json
# numbers = [2, 3, 5, 7, 11, 13,15,17]
# filename = 'numbers.json'
# with open(filename,'r+') as f_obj:
#     data=json.dump(numbers,f_obj)
#     data1=json.load(f_obj)
# print(data1)
# print(data[0])
# username = input("What is your name? ")
username = {'name': 'mans', 'id': 30557, 'address': 'sdh', 'balance': 'Rs 888'}
filename = 'username.json'
with open(filename,'a') as f_obj:
     json.dump(str(username)+"\n", f_obj)
    # username=json.load(f_obj)
    # print("We'll remember you when you come back, " + str(user) + "!")
    # print(username)
    # if 'Rs 999' in username:
    #     print(username)
