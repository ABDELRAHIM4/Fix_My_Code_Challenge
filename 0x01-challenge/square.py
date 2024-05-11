#!/usr/bin/python3
"""class square"""


class Square:
    """class square"""
    def __init__(self, width = 0, height = 0):
        self._width = width
        self._height = height

    def area(self):
        """ Area of the square """
        return self._width * self._width

    def perimeter(self):
        return (self._width * 4)


    def __str__(self):
        return ("Square width {}".format(self._width))


if __name__ == "__main__":

    s = Square(width=12)
    print(s)
    print(s.area())
    print(s.perimeter())
