from shape import Shape
import math

# Triangle class is child class of Shape parent class

class Triangle(Shape):
    def __init__(self):
        super().__init__("triangle")
        self.__base = None
        self.__height = None

    # helper functions to do error checking in set method
    def set_base(self, base):
        if not isinstance(base, float) and not isinstance(base, int):
            raise TypeError("Only float numbers can be used for length of base of triangle.")
        if not base > 0:
            raise ValueError("Only positive numbers can be used for length of base of triangle.")

        self.__base = base

    def set_height(self, height):
        if not isinstance(height, float) and not isinstance(height, int):
            raise TypeError("Only float numbers can be used for length of height of triangle.")
        if not height > 0:
            raise ValueError("Only positive numbers can be used for length of height of triangle.")

        self.__height = height

    # area method to return area of triangle
    def area(self):
        if self.__base is None:
            raise TypeError("Length of base of triangle needs to be set")
        if self.__height is None:
            raise TypeError("Length of height of triangle needs to be set")

        return .5 * self.__base * self.__height

    # perimeter method to return perimeter of triangle
    def perimeter(self):
        if self.__base is None:
            raise TypeError("Length of base of triangle needs to be set")
        if self.__height is None:
            raise TypeError("Length of height of triangle needs to be set")
        return round(self.__base + 2 * math.pow(.25 * self.__base * self.__base + self.__height * self.__height, .5), 2)

    # method to print the name of the shape followed by the area and perimeter of shape
    def draw(self):

        super().draw()
