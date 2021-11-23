from shape import Shape


# Circle class is child class of Shape parent class

class Circle(Shape):
    def __init__(self):
        super().__init__("circle")
        self.__radius = None

    """
    Helper function set_radius to do error checking in set method
    param:  
    :radius: int or float
    
    """
    def set_radius(self, radius):
        if not isinstance(radius, float) and not isinstance(radius, int):
            raise TypeError("Only float numbers can be used for radius of circle.")
        if not radius > 0:
            raise ValueError("Only positive numbers can be used for radius of circle.")

        self.__radius = radius

    """
    Area method to return area of circle
    param:  None
    return:  area of circle
        
    """
    def area(self):
        if self.__radius is None:
            raise TypeError("Length of radius needs to be set")

        return 3.14159 * self.__radius * self.__radius

    """
    Perimeter/circumference method to return circumference of cirlce
    param:  None   
    return: circumference or perimeter of circle
    
    """
    def perimeter(self):
        if self.__radius is None:
            raise TypeError("Length of radius needs to be set")
        return 2 * self.__radius * 3.14159

    """
    Method to print the name of the shape followed by the area and perimeter of shape
    param:  None   
    return: name of shape, area of shape, perimeter of shape

    """
    def draw(self):

        super().draw()


# driver code to test above

# mycircle = Circle()
# mycircle.set_radius(1)
# myarea = mycircle.area()
# print(myarea)
# myperimeter = mycircle.perimeter()
# print(myperimeter)
# mycircle.draw()


    