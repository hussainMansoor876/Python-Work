bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(len(bicycles))
print(bicycles[1])
print(bicycles[-4])
bicycles[0]='honda'
print(bicycles)
bicycles.append('yamaha')
print(bicycles)
bicycles.extend("corolla")
bicycles.append("corolla")
print(bicycles)
del bicycles[0]
print(bicycles)
bicycles.pop(0)
print(bicycles)
first_owned=bicycles.pop()
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
bicycles.remove('c')
print(bicycles)
print(sorted(bicycles))
print(bicycles)
bicycles.sort()
print(bicycles)
bicycles.sort(reverse=True)
print(bicycles)
bicycles.reverse()
print(bicycles)
print(len(bicycles))
print(bicycles[6])