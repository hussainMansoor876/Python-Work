student={"name":"Mansoor","Father name":"Manzoor Hussain","Class":"3rd year","age":19}
for key,value in student.items():
    print(key+':'+str(value))
for k in student:
    print('my '+k+' is '+str(student[k]))
for v in student.values():
    print(v)
for v in sorted(str(student.values())):
    print(str(v))