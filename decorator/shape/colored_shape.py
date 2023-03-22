class ColoredShape:
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        pass

    def __str__(self):
        pass

class ColoredShape:
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        getResize = getattr(self.shape, 'resize', None)
        if callable(getResize):
            self.shape.resize(factor)

    def __str__(self):
        return f'{str(self.shape)} has the color {self.color}'
