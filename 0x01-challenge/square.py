#!/usr/bin/python3
"""class square"""


class Square:
    """class square"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """ Area of the square """
        return self.width * self.width

    def Perimeter(self):
        return (self.width * 4)


    def __str__(self):
        return ("{}/{}".format(self.width, self.height))


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area())
    print(s.Perimeter())
