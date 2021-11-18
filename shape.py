#abstract base class Shape parent class to child classes Circle, Square, Rectangle, Triangle
import abc

class Shape(metaclass=abc.ABCMeta):
    #constructor
    def __init__(self, name):
        self.__name = name

    #method for equality operator to help sort shapes by area
    def __eq__(self, other):
        if not isinstance(other, Shape): raise TypeError
        return self.area() == other.area()

    #method for less than operator to help sort shapes by area
    def __lt__(self, other):
        if not isinstance(other, Shape):
            raise TypeError("Only Shape objects can be compared.")
        return self.area() < other.area()

    #getter function to return name
    def name(self):
        return self.__name

    # property to get the name of the shape
    name = property(name)

    #abstract method that will return the area of the given shape
    @abc.abstractmethod
    def area(self):
        pass

    #abstract method that will return the perimeter of the given shape
    @abc.abstractmethod
    def perimeter(self):
        pass

    #method that prints the name of the shape followed by the area and perimeter of the
    #shape formatted as follows: "name_of_shape, area: value_of_area, perimeter: value_of_perimeter"
    def draw(self):
        print(self.__str__())

    #to string method that would allow draw() to call this method and print out the results
    def __str__(self):
        return str(self.__name) + ", area: " + str(self.area()) + ", perimeter: " + str(self.perimeter())
