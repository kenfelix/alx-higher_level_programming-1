#!/usr/bin/python3

"""
Module 9-rectangle
Defines a rectangle
Handles square
"""


class Rectangle:
    """
    Defines a rectangle
    Private attributes width and height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize width and height """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Accesses the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Mutates the width
        Args:
            value (int): new width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Accesses the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Mutates the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """ Returns perimeter of a rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2*(self.width + self.height)

    def __str__(self):
        """return string object of rectangle with #"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width
                          for row in range(self.height)])

    def __repr__(self):
        """Returns canonical string representation
            of a rectangle with #"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ Prints a message when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        # this works -> return cls(size, size)
        return Rectangle(size, size)
