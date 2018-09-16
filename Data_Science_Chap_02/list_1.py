integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [ integer_list, heterogeneous_list, [] ]
list_len=len(integer_list)
list_sum=sum(integer_list)
print(list_of_lists)
print(list_len)
print(list_sum)
integer_list.extend([4,5,6])
print(integer_list)