class Dog():
    def __init__(self,nick,month):
        self.name = nick
        self.age = month
    def name1(self):
        print("My dog's name is " + my_dog.name.title() + ".")
        print("My dog is " + str(my_dog.age) + " years old.")
    def sit(self):
        print(self.name,"is siting")
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
my_dog.sit()
my_dog.name1()
your_dog.sit()
your_dog.name1()