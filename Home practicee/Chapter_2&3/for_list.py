squares=[value**2 for value in range(1,11)]
print(squares)
print(squares[2])
print(squares[:2])
print(squares[::2])
print(squares[1::2])
square=squares[1:6]
print(square)
if 4 in squares:
    print("yes")
else:
    print("no")