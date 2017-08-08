# Question:
# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
#
# Hints:
#
# Use def methodName(self) to define a method
import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        area = math.pi * self.radius * self.radius
        print("Area = ",area)
a = Circle(5)
a.area()
