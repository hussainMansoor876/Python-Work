import re
password=input("Enter string to test:")
words=password.split(".")
if (words):
    for word in words:
        pattern="^.*(?=.{6,12})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.[@#$%^&+=]).*$"
        result=re.findall(pattern,word)
        if(result):
            print(word+"Valid")
            break
        else:
            print(print(word+"Not Valid"))