from shape import Shape


class Rectangle(Shape):

    def __init__(self, ln, w):
        super().__init__("rectangle")
        self.__length = ln
        self.__width = w

    def perimeter(self):
        return (self.__length * 2) + (self.__width * 2)

    def area(self):
        return self.__length * self.__width


r = Rectangle(3, 4)
print(r)
