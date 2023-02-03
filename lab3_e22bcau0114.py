class Shape:
    def __init__(self,c,x,y):
        self.color=c
        self.l=x
        self.b=y
    def area(self):
        return self.l*self.b
    def colour(self):
        return self.color

class Square(Shape):
    def __init__(self,c,x):
        super().__init__(c,x,x)

class Rectangle(Shape):
    def __init__(self,c,x,y):
        super().__init__(c,x,y)

a=Square("Red",5)
b=Rectangle("Green",5,10)
print(a.area())
print(a.colour())
print(b.area())
print(b.colour())