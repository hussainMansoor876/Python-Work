squares=[]
for square in range(0,11):
    print("Square of "+str(square)+" is "+str(square**2))
    square=square**2
    squares.append(square)
print(squares)
print(len(squares))
print(min(squares))
print(max(squares))
print(list(squares))
print(list(reversed(squares)))
squares.reverse()
print(squares)