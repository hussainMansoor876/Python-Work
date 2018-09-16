from collections import Counter
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
def not_the_same(user,other_user):
    return user["id"] != other_user["id"]
'''def not_friends(user, other_user):
    """other_user is not a friend if he's not in user["friends"];
    that is, if he's not_the_same as all the people in user["friends"]"""
    return all(not_the_same(friend, other_user)
                for friend in user["friends"])'''
def not_friends(user,other_user):
    name1=[]
    for friend in user['friends']:
        name1.append(not_the_same(friend,other_user))
        print(name1)
    return all(name1)

def friends_of_friend_ids(user):
    return Counter(foaf["name"]
    for friend in user["friends"] # for each of my friends
        for foaf in friend["friends"] # count *their* friends
            if not_the_same(user, foaf) # who aren't me
            and not_friends(user, foaf)) # and aren't my friends
print(friends_of_friend_ids(users[0]))
#total_connections = sum(number_of_friends(user) for user in users)
#print(total_connections)
#num_users = len(users) # length of the users list
#avg_connections = total_connections / num_users
#print(avg_connections)
#num_friends_by_id = [(user["id"], number_of_friends(user))
                    #for user in users]
#print(num_friends_by_id)

'''def friends_of_friend_ids_bad(user):
    return [(foaf['id'],foaf["name"])
        for friend in user["friends"]
        for foaf in friend["friends"]]'''
'''for user in users:
    friend1_oaf=friends_of_friend_ids(user)
    n_friends=not_friends(user,users[0])
print(friend1_oaf)'''