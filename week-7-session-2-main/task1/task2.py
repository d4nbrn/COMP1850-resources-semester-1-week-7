class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"This object is at x-coordinate: {self.x} and y coordinate: {y}"
    def __repr__(self):
        return f"x:{self.x} y:{self.y}"
# Given a Point class, define the __str__ and __repr__ methods
