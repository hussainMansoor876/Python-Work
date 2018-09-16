import re
regex = r"[a-zA-Z]+"
email=str(input("Enter email:"))
matches = re.findall(regex,email)
print(matches[0])