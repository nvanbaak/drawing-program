# nvb / 17 Nov 2021
# code for DrawingProgram class

from shape import Shape

class DrawingProgram:
    def __init__(self, shape_list=[]):
        
        # validate input
        for shape in shape_list:
            if not isinstance(shape, Shape):
                raise TypeError("Not a shape!")
        self.shape_list = shape_list

    def addShape(self, shape):
        """
        Adds a Shape object to the list of shapes.

        params:
        :shape: a Shape object to add.
        """
        pass

    def remove_shape(self, shape):
        """
        Removes all Shape objects matching the given Shape object.

        params:
        :shape: the Shape object to remove.
        :returns: the number of objects removed.
        """
        pass

    def print_shape(self, shape):
        """
        Prints all Shapes matching the given Shape object.

        params: the given Shape object.
        :returns: None 
        """
        pass

    def sort_shapes(self):
        """
        Sorts the list of shapes.

        :returns: None 
        """
        pass

    def __str__(self):
        """
        Returns a string represetation of each Shape object
        in shape_list.
        """
        pass

    def get_shape(self, index):
        """
        Returns the Shape object at the specified index.
        
        params:
        :index: an integer of size no greater than the number of shapes
                in shape_list
        :returns: the Shape at the given index, or None if none exists
        """
        pass

    def set_shape(self, index, shape):
        """
        Given an index and a Shape object, sets the Shape
        at that index to the given Shape.

        params:
        :index: an integer of size no greater than the number of shapes
                in shape_list
        :shape: the Shape object to set to.
        :returns: None
        """
        pass


