#!/usr/bin/python3
"""class square"""


class square():
    """class square"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def Permiter_Of_My_Square(self):
        return (self.width * 4)


    def __str__(self):
        return ("{}/{}".format(self.width, self.height))


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.Permiter_Of_My_Square())
