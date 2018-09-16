
try:
    num1 = int(input("Enter number:"))
    num2 = int(input("Enter number:"))
    num3 = num1 / num2
    print(num3)
except ZeroDivisionError:
    print("You can't divide by zero")