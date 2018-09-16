class dog():
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
    def bark(self):
        print(self.name,"is barking")
        print(self.name,'is',self.age,'years old')
    def run(self):
        print("Dog is running")
    def col(self):
        print('My',self.name,'color is',self.color)
d=dog('willie','6','green')
d.bark()
d.run()
d.col()