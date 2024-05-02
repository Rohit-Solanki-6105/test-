'''
9. Create an interface Shape with methods area() and perimeter().
'''
from abc import ABC, abstractmethod

# Define abstract base class Shape with abstract methods area() and perimeter()
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Example usage with a concrete subclass Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2  # Calculate area of circle

    def perimeter(self):
        return 2 * 3.14 * self.radius  # Calculate perimeter (circumference) of circle

# Example usage with a concrete subclass Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  # Calculate area of rectangle

    def perimeter(self):
        return 2 * (self.length + self.width)  # Calculate perimeter of rectangle

circle = Circle(5)
print("Circle - Area:", circle.area())
print("Circle - Perimeter:", circle.perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle - Area:", rectangle.area())
print("Rectangle - Perimeter:", rectangle.perimeter())

'''
Circle - Area: 78.5
Circle - Perimeter: 31.400000000000002
Rectangle - Area: 24
Rectangle - Perimeter: 20
'''