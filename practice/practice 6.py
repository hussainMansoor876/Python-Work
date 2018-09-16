import re
regex = r"[a-zA-Z]+ \d+"
matches = re.findall(regex, "June 24,August 5")
for match in matches:
    print("Match month:",(match))