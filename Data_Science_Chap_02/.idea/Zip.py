list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3=list(zip(list1, list2))
print(list3)
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
print(letters)
print(numbers)