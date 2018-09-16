student={"name":"Mansoor","Father name":"Manzoor Hussain","Class":"3rd year","age":19}
print(student['age'])
print('i am '+str(student['age'])+' years old.')
student['subject']='Fundamental programming'
print(student)
del student['subject']
print(student)
print(len(student))
print(list(student))
print(list(student.items()))
print(list(student.values()))