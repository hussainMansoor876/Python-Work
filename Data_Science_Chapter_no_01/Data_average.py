users=[{'id':0,'name':'Mansoor'},
{'id':1,'name':'Ahsan'},
{'id':2,'name':'Ali'},
{'id':3,'name':'Ahmed'},
{'id':4,'name':'Mujhid'}
]
friendship=[(0,1),(0,2),(1,2),(1,4),(2,3)]
for user in users:
    user["friends"] = []
for i,j in friendship:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])
    #print(users)
def number_of_friends(user):
    return len(user["friends"])
total_connections = sum(number_of_friends(user) for user in users)
#print(total_connections)
num_users = len(users) # length of the users list
avg_connections = total_connections / num_users
print(avg_connections)
#num_friends_by_id = [(user["name"],number_of_friends(user))
                    #for user in users]
#print(num_friends_by_id)
num1_friends=[]
for user in users:
    num2_friends=user['name'],number_of_friends(user)
    num1_friends.append(num2_friends)
print(num1_friends)