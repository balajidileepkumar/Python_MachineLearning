class Pen():
    def __init__(self):
        self.color = "red"
        self.pentype = "refill"
    
    def writedata(self):
       print(type(self), self.color, self.pentype)

class BallPointPen(Pen):
    def __init__(self):
        self.color = "red"
        self.pentype = "Ball Point"
    
    def writedata(self):
       print(type(self), self.color, self.pentype)

class Pencil():
    def __init__(self):
        self.color = "red"
        self.pentype = "Ball Point"
    
    def writedata(self):
       print(type(self), self.color, self.pentype)
    
a=Pen()
print(type(a))
a.writedata()

print(isinstance(a, Pen))

b = BallPointPen()
print(issubclass(BallPointPen,Pen))

c = Pencil()
print(issubclass(Pencil,Pen))


import inspect 
print("#############using inspect################")
print(inspect.isclass(c))
y = 10
print(inspect.isclass(y))

print(inspect.isclass(Pencil))