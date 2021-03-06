from shape import Shape


# Rectangle class is child class of Shape parent class

class Rectangle(Shape):
    def __init__(self):
        super().__init__("rectangle")
        self.__length = None
        self.__width = None

    """
    Helper function to do error checking of rectangle length in set method
    param:    
    :length:  int or float    
    return: None
    
    """
    def set_length(self, length):
        if not isinstance(length, float) and not isinstance(length, int):
            raise TypeError("Only float numbers can be used for length of rectangle.")
        if not length > 0:
            raise ValueError("Only positive numbers can be used for length of rectangle.")

        self.__length = length

    """
    Helper function to do error checking of rectangle width in set method
    param:  
    :width: int or float   
    return: None

    """
    def set_width(self, width):
        if not isinstance(width, float) and not isinstance(width, int):
            raise TypeError("Only float numbers can be used for width of rectangle.")
        if not width > 0:
            raise ValueError("Only positive numbers can be used for width of rectangle.")

        self.__width = width

    """
    Area method to return area of rectangle
    param:  None   
    return: area of rectangle

    """
    def area(self):
        if self.__length is None:
            raise TypeError("Length of rectangle needs to be set")
        if self.__width is None:
            raise TypeError("Width of rectangle needs to be set")

        return self.__length * self.__width

    """
    Perimeter method to return perimeter of rectangle
    param:  None   
    return:  perimeter of rectangle
    
    """
    def perimeter(self):
        if self.__length is None:
            raise TypeError("Length of side needs to be set")
        if self.__width is None:
            raise TypeError("Width of rectangle needs to be set")

        return 2 * self.__length + 2 * self.__width

    """
    Method to print the name of the shape followed by the area and perimeter of shape
    param:  None   
    return: name of shape, area of shape, perimeter of shape

    """
    def draw(self):

        super().draw()


# driver code to test above

# myrectangle = Rectangle()
# myrectangle.set_length(1)
# myrectangle.set_width(2)
# myarea = myrectangle.area()
# print(myarea)
# myperimeter = myrectangle.perimeter()
# print(myperimeter)
# myrectangle.draw()
