# nvb / 17 Nov 2021
# code for DrawingProgram class

from dp_iter import DrawingProgramIterator
from shape import Shape

class DrawingProgram:
    """
    A class that handles a collection of shapes
    """
    class DrawingProgramIterator:
        def __init__(self, shape_list):
            self._index = 0
            self._shape_list = shape_list

        def __next__(self):
            output = self._shape_list[self._index]
            if self._index >= len(self._shape_list):
                raise StopIteration
            return output

    def __init__(self, shape_list=None):
        # validate input
        if shape_list is None:
            self.shape_list = []
        else:
            for shape in shape_list:
                if not isinstance(shape, Shape):
                    raise TypeError("Not a shape!")
            self.shape_list = shape_list

    def __iter__(self):
        return DrawingProgramIterator(self.shape_list)

    def addShape(self, shape):
        """
        Adds a Shape object to the list of shapes.

        params:
        :shape: a Shape object to add.
        """
        if isinstance(shape, Shape): 
            self.shape_list.append(shape)
        else:
            raise(TypeError, "Attempted to add a non-Shape object to DrawingProgram!")

    def remove_shape(self, shape):
        """
        Removes all Shape objects matching the given Shape object.

        params:
        :shape: the Shape object to remove.
        :returns: the number of objects removed.
        """

        # get length of shape_list
        endpoint = len(self.shape_list)

        # trivial case for empty list
        if endpoint == 0: return 0

        # otherwise iterate
        deletions = 0

        while endpoint > 0:
            endpoint -= 1
            if self.shape_list[endpoint] == shape:
                self.shape_list.pop(endpoint)
                deletions += 1

        return deletions

    def print_shape(self, shape):
        """
        Prints all Shapes matching the given Shape object.

        params: the given Shape object.
        :returns: None 
        """
        for element in self.shape_list:
            if element == shape:
                print(element.__str__())

    def __str__(self):
        """
        Returns a string represetation of each Shape object
        in shape_list.
        """
        output = ""
        for sh in self.shape_list:
            output += sh.__str__() + "\n"
        return output

    def get_shape(self, index):
        """
        Returns the Shape object at the specified index.
        
        params:
        :index: a positive integer of size no greater than the number of shapes in shape_list
        :returns: the Shape at the given index, or None if none exists
        """
        if not index in range(0, len(self.shape_list)):
            raise IndexError("Index out of bounds!")

        return self.shape_list[index]

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

        # validate input
        if not index in range(0, len(self.shape_list)):
            raise IndexError("Index out of bounds!")
        if not isinstance(shape, Shape):
            raise TypeError("Not a Shape object!")

        self.shape_list[index] = shape

    def sort_shapes(self):
        """
        Sorts the list of shapes.

        :returns: None 
        """

        self.shape_list = self.merge_sort(self.shape_list)

    def merge_sort(self, list):
        """
        Recursive merge sort implementation shamelessly copy-pasted from nvb's Homework 2.  Given a list object, returns a sorted list object with the same elements.
        """

        list_len = len(list)
        
        # base cases
        if list_len == 0: return []
        if list_len == 1: return list

        # recursive case

        # divide list in half
        midpoint = list_len // 2
        list_A = self.merge_sort(list[:midpoint])
        list_B = self.merge_sort(list[midpoint:])

        # set up variables
        sorted_list = []
        num_sorted = 0

        idx_A = 0
        len_A = len(list_A)
        sorted_A = False
        
        idx_B = 0
        len_B = len(list_B)
        sorted_B = False

        while num_sorted < list_len:

            # if either list is exhausted, grab from the other
            if sorted_A:
                sorted_list.append(list_B[idx_B])
                idx_B += 1

            elif sorted_B:
                sorted_list.append(list_A[idx_A])
                idx_A += 1

            # if neither is exhausted, compare the lowest of each
            else:
                if list_A[idx_A] < list_B[idx_B]:
                    sorted_list.append(list_A[idx_A])
                    idx_A += 1
                    if idx_A >= len_A:
                        sorted_A = True
                else:
                    sorted_list.append(list_B[idx_B])
                    idx_B += 1
                    if idx_B >= len_B:
                        sorted_B = True
            
            # increment the count
            num_sorted += 1

        return sorted_list