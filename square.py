from shape import Shape


# Square class is child class of Shape parent class

class Square(Shape):
    def __init__(self):
        super().__init__("square")
        self.__length_of_side = length_of_side

    #do error checking in set method
    def set_side(self, length_of_side):
        if not self.__length_of_side > 0:
            raise ValueError("Only positive numbers can be used for length of side of square.")
        if not self.__length_of_side is float:
            raise TypeError("Only float numbers can be used for length of side of square.")
        return length_of_side

    # area method to return area of square
    def area(self):

        # assert isinstance(value_of_area, float)
        return self.__length_of_side * self.__length_of_side

    # perimeter method to return perimeter of square
    def perimeter(self):
        if not self.__length_of_side > 0:
            raise ValueError("Only positive numbers can be used for length of side of square.")

        return 4 * self.__length_of_side

    # method to print the name of the shape followed by the area and perimeter of shape
    def draw(self):
        #print(super().name(), ", area: ", self.area(), ", perimeter: ", self.perimeter())
        super().draw()


    
# driver code to test above
length_of_side = 4
mysquare = Square()

myarea = mysquare.area()
print(myarea)
myperimeter = mysquare.perimeter()
print(myperimeter)
mysquare.draw()
