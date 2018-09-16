class Dog():
    def __init__(self,nick,month):
        print("Hello")
        self.nume = nick
        self.old = month
    def name(self):
        print("My dog name is",self.nume)
        print(self.old,'years old')
my_dog = Dog('willie',7)
my_dog.name()
