#!/usr/bin/python3
"""class square"""


class Square:
    """class square"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        """ Area of the square """
        return (self.__width * self.__height)

    def perimeter(self):
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        return ("{}/{}".format(self.__width, self.__height))


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print("Area:", s.area())
    print("perimeter: ", s.perimeter())
