try:
    n=int(input("Enter number"))
    f=(n+1)/(n-1)
    print(f)
except ZeroDivisionError:
    print("you can't divide by zero")