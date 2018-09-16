# with open('text.py') as fileObj:
#     content=fileObj.readline(2)
#     print(content)
filename='programming.txt'
with open(filename,'a') as file:
    file.write(input("Enter something here :")+" ")
with open(filename) as file:
    lines=file.read()
for line in lines.splitlines():
    print(line)