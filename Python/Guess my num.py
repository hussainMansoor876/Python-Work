from random import  randint
for number in range(1,10):
    num=randint(1,50)
    count=0
    for val in range(1,4):
        num1=int(input("Enter number:\n"))
        if(num1==num):
            count+=1
            print("You won in",count,"tries")
            break
        elif(num1<num):
            count += 1
            if(count==3):
                break
            print("You guess is too low please Try again")
        elif(num1>num):
            count += 1
            if(count==3):
                break
            print("Your guess is too high please try again")
    if(count==3):
        print("Oops! you loose in three tries")
    game=int(input("Do you want to play again\n1.Yes\n2.No\n"))
    if(game==1):
        print("New game")
    else:
        break
print("Exit the game")

