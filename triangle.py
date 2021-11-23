from shape import Shape
import math

# Triangle class is child class of Shape parent class

class Triangle(Shape):
    def __init__(self):
        super().__init__("triangle")
        self.__base = None
        self.__height = None

    """
    Helper function to do error checking of triangle base in set method
    param:    
    :base:  int or float    
    return: None

    """
    def set_base(self, base):
        if not isinstance(base, float) and not isinstance(base, int):
            raise TypeError("Only float numbers can be used for length of base of triangle.")
        if not base > 0:
            raise ValueError("Only positive numbers can be used for length of base of triangle.")

        self.__base = base

    """
    Helper function to do error checking of triangle height in set method
    param:    
    :height:  int or float    
    return: None

    """
    def set_height(self, height):
        if not isinstance(height, float) and not isinstance(height, int):
            raise TypeError("Only float numbers can be used for length of height of triangle.")
        if not height > 0:
            raise ValueError("Only positive numbers can be used for length of height of triangle.")

        self.__height = height

    """
    Area method to calculate and return area of triangle
    param:  None 
    return:  area of triangle

    """
    def area(self):
        if self.__base is None:
            raise TypeError("Length of base of triangle needs to be set")
        if self.__height is None:
            raise TypeError("Length of height of triangle needs to be set")

        return .5 * self.__base * self.__height

    """
    Perimeter method to calculate and return perimeter of triangle
    param:  None 
    return:  perimeter of triangle in terms of base and height, derived using Pythagorean's Theorem

    """
    def perimeter(self):
        if self.__base is None:
            raise TypeError("Length of base of triangle needs to be set")
        if self.__height is None:
            raise TypeError("Length of height of triangle needs to be set")
        return round(self.__base + 2 * math.pow(.25 * self.__base * self.__base + self.__height * self.__height, .5), 2)

    """
    Method to print the name of the shape followed by the area and perimeter of shape
    param:  None    
    return: name of shape, area of shape, perimeter of shape

    """
    def draw(self):

        super().draw()


# driver code to test above

# mytriangle = Triangle()
# mytriangle.set_base(1)
# mytriangle.set_height(1)
# myarea = mytriangle.area()
# print(myarea)
# myperimeter = mytriangle.perimeter()
# print(myperimeter)
# mytriangle.draw()
