import math

class Shape:
    def name(self):
        """
        This method returns the name of the shape.
        The base Shape class always returns the string "Shape".
        Subclasses (like Square) will override this method.
        """
        pass

class Square(Shape):
    def name(self):
        """
        This overrides the parent class (Shape) name() method.
        Because this is a Square, it must return the string "Square".
        This demonstrates polymorphism: same method name, different behavior.
        """
        pass

class Circle:
    def __init__(self, radius):
        """
        The constructor receives a radius value.
        It must be stored in an instance variable called self.radius.
        The tests check that the radius is stored correctly.
        """
        pass

    def area(self):
        """
        This method calculates the area of a circle.
        The formula is: π × radius².
        VERY important: use self.radius, not just 'radius',
        because radius is not a local variable.
        """
        pass

class Rectangle:
    def __init__(self, width, height):
        """
        The constructor receives width and height.
        Both values must be saved to instance variables:
        - self.width
        - self.height
        The tests check that these are stored correctly.
        """
        pass

    def area(self):
        """
        This method returns the area of the rectangle.
        Formula: width × height.
        The tests expect this exact calculation.
        """
        pass