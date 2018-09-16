import re
num=r"\d+"
matches = re.findall(num,"2 Cats,3 Dogs")
match1=[]
for match in matches:
    print(match)
    match1.append(match)
print(match1)