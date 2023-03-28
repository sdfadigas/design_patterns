class Circle:
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return 'A circle of radius %s' % self.radius
    
class ColoredShape:
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        pass

    def __str__(self):
        pass

class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return 'A square with side %s' % self.side
    
circle = ColoredShape(Circle(5), 'red')
print(circle)
circle.resize(2)
print(circle)

square = ColoredShape(Square(2), 'blue')
print(square)
square.resize(2)
print(square)