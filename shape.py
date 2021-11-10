#abstract base class Shape parent class to child classes Circle, Square, Rectangle, Triangle
import abc

class Shape(metaclass=abc.ABCMeta):
    #constructor
    def __init__(self, name):
        self.__name = name

    #abstract method that will return the area of the given shape
    @abc.abstractmethod
    def area(self):
        pass

    #abstract method that will return the perimeter of the given shape
    def perimeter(self):
        pass

    #method that prints the name of the shape followed by the area and perimeter of the
    #shape formatted as follows: "name_of_shape, area: value_of_area, perimeter: value_of_perimeter"
    def draw(self):
        pass

    #to string method that would allow draw() to call this method and print out the results
    #def __str__(self, name, value_of_area, value_of_perimeter):
        #return str(self.__name) + "," + str(self.__value_of_area) + "," + str(self.__value_of_perimeter)
