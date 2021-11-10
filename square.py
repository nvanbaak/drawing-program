from shape import Shape


# Square class is child class of Shape parent class

class Square(Shape):
    def __init__(self, name, length_of_side: float):
        # super().__init__()
        self.__name = name
        self.__length_of_side = length_of_side


    # area method to return area of square
    def area(self, length_of_side):
        if not length_of_side > 0:
            raise ValueError("Only positive numbers can be used for length of side of square.")
        value_of_area = length_of_side * length_of_side
        # assert isinstance(value_of_area, float)
        return value_of_area

    # perimeter method to return perimeter of square
    def perimeter(self, length_of_side):
        if not length_of_side > 0:
            raise ValueError("Only positive numbers can be used for length of side of square.")
        value_of_perimeter = 4 * length_of_side
        return value_of_perimeter

    # method to print the name of the shape followed by the area and perimeter of shape
    def draw(self, name):
        print(name, ", area: ", self.area(length_of_side), ", perimeter: ", self.perimeter(length_of_side))


# driver code to test above

mysquare = Square("square", 4)
length_of_side = 4
myarea = mysquare.area(length_of_side)
print(myarea)
myperimeter = mysquare.perimeter(length_of_side)
print(myperimeter)
mysquare.draw("square")
