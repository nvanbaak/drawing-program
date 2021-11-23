from shape import Shape


# Square class is child class of Shape parent class

class Square(Shape):
    def __init__(self):
        super().__init__("square")
        self.__length_of_side = None

    """
    Helper function to do error checking of length of side of square in set method
    param:    
    :length_of_side:  int or float    
    return: None

    """
    def set_side(self, length_of_side):
        if not isinstance(length_of_side, float) and not isinstance(length_of_side, int):
            raise TypeError("Only float numbers can be used for length of side of square.")
        if not length_of_side > 0:
            raise ValueError("Only positive numbers can be used for length of side of square.")

        self.__length_of_side = length_of_side

    """
    Area method to return area of square
    param:  None 
    return:  Area of square
    
    """
    def area(self):
        if self.__length_of_side is None:
            raise TypeError("Length of side needs to be set")
        return self.__length_of_side * self.__length_of_side

    """
    Perimeter method to return perimeter of square
    param:  None        
    return: perimeter of square
    
    """
    def perimeter(self):
        if self.__length_of_side is None:
            raise TypeError("Length of side needs to be set")
        return 4 * self.__length_of_side

    """
    Method to print the name of the shape followed by the area and perimeter of shape
    param:  None  
    return: name of shape, area of shape, perimeter of shape

    """
    def draw(self):

        super().draw()


    
# driver code to test above
# mysquare = Square()
# mysquare.set_side(4)
# myarea = mysquare.area()
# print(myarea)
# myperimeter = mysquare.perimeter()
# print(myperimeter)
# mysquare.draw()
