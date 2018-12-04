import math

class Circle():
    def __init__(self, initialRadius=1):
        self.radius = initialRadius
        self.diameter = 2 * self.radius
        self.area = math.pi * self.radius ** 2
