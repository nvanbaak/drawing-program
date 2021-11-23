#abstract base class Shape parent class to child classes Circle, Square, Rectangle, Triangle
import abc

class Shape(metaclass=abc.ABCMeta):
    """
    Constructor
    """
    def __init__(self, name):
        self.__name = name

    """
    Method for equality operator to help sort shapes by area
    param:    
    :other:  another object member of Shape class    
    return: Boolean

    """
    def __eq__(self, other):
        if not isinstance(other, Shape): raise TypeError("Not a Shape object!")
        return self.area() == other.area()

    """
    Method for less than operator to help sort shapes by area
    param:    
    :other:  another object member of Shape class    
    return: Boolean

    """
    def __lt__(self, other):
        if not isinstance(other, Shape):
            raise TypeError("Only Shape objects can be compared.")
        return self.area() < other.area()

    """
    Getter function to return name
    param:  None    
    return: name of the shape

    """
    def get_name(self):
        return self.__name

    """
    Property to get the name of the shape
    """
    name = property(get_name)

    """
    Abstract method that will return the area of the given shape
    param:  None    

    """
    @abc.abstractmethod
    def area(self):
        pass

    """
    Abstract method that will return the perimeter of the given shape
    param:  None    
    
    """
    @abc.abstractmethod
    def perimeter(self):
        pass

    """
    Method that prints the name of the shape followed by the area and perimeter of the shape formatted
    as follows: "name_of_shape, area: value_of_area, perimeter: value_of_perimeter"
    param:  None    
    return: name of shape, area of shape, perimeter of shape formatted as described above
    """
    def draw(self):
        print(self.__str__())

    """
    To string method that would allow draw() to call this method and print out the results
    param: None    
    return: name of shape, area of shape, perimeter of shape

    """
    def __str__(self):
        return str(self.__name) + ", area: " + str(self.area()) + ", perimeter: " + str(self.perimeter())
