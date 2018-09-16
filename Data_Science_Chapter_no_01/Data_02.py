users = [
{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }
]
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
for user in users:
    user["friends"] = []
    #print(user)
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])
    print(users)
def number_of_friends(user):
    return len(user['friends'])
total_connections=[number_of_friends(user) for user in users]
print(total_connections)
print(sum(total_connections))
'''sum_of_friends=[]
for user in users:
    friends=number_of_friends(user)
    sum_of_friends.append(friends)
    print(sum_of_friends)
print(sum(sum_of_friends))'''
num_user=len(users)
print(num_user)
average=sum(total_connections)/num_user
print(average)