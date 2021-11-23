from shape import Shape


# Square class is child class of Shape parent class

class Square(Shape):
    def __init__(self):
        super().__init__("square")
        self.__length_of_side = None

    #helper function to do error checking in set method
    def set_side(self, length_of_side):
        if not isinstance(length_of_side, float) and not isinstance(length_of_side, int):
            raise TypeError("Only float numbers can be used for length of side of square.")
        if not length_of_side > 0:
            raise ValueError("Only positive numbers can be used for length of side of square.")

        self.__length_of_side = length_of_side

    # area method to return area of square
    def area(self):
        if self.__length_of_side is None:
            raise TypeError ("Length of side needs to be set")
        # assert isinstance(value_of_area, float)
        return self.__length_of_side * self.__length_of_side

    # perimeter method to return perimeter of square
    def perimeter(self):
        if self.__length_of_side is None:
            raise TypeError("Length of side needs to be set")
        return 4 * self.__length_of_side

    # method to print the name of the shape followed by the area and perimeter of shape
    def draw(self):
        #print(super().name(), ", area: ", self.area(), ", perimeter: ", self.perimeter())
        super().draw()
