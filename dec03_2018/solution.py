import math

class Circle():
    @property
    def radius(self):
        return self.radius
    
    @radius.setter
    def radius(self, newRadius):
        self.radius = newRadius
        self.diameter = 2*newRadius
        self.area = math.pi * newRadius**2

    def __init__(self, initialRadius=1):
        self.radius = initialRadius
