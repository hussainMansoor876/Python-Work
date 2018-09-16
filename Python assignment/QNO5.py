class Square():
    def __init__(self,length):
        self.length=length
        self.area=self.length*self.length
    def area1(self):
        print("Area of square is:",self.area)
d=Square(int(input("Enter length")))
d.area1()
class Square1(Square):
    def __init__(self,length):
        super().__init__(length)
    def area1(self):
        print("area of super class square is:",self.area)
s=Square1(int(input("Enter length")))
s.area1()