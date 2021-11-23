from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle

class ShapeFactory:
    """
    A static class containing the methods for creation of Shape objects.
    """

    @staticmethod
    def create_shape(shape_name, *args):
        """
        A method for creating Shape objects according to user-generated paramters.

        params:
        :shape_name: the name of the Shape object to create
        :args: parameter information with meaning dependent on the Shape:
            Rectangle: width, height
            Square: side length
            Triangle: width, height
            Circle: radius
        :returns: a Shape
        """
        shape_data = args
        count = len(args)
        if shape_name == "rectangle":
            if count != 2:
                raise ValueError(f"Two arguments expected for {shape_name}. Actual: {count}")
            r = Rectangle()
            r.set_width(shape_data[0])
            r.set_length(shape_data[1])
            return r
        elif shape_name == "square":
            if count != 1:
                raise ValueError(f"One argument expected for {shape_name}. Actual: {count}")
            s = Square()
            s.set_side(shape_data[0])
            return s
        elif shape_name == "triangle":
            if count != 2:
                raise ValueError(f"Two arguments expected for {shape_name}. Actual: {count}")
            t = Triangle()
            t.set_base(shape_data[0])
            t.set_height(shape_data[1])
            return t
        elif shape_name == "circle":
            if count != 1:
                raise ValueError(f"One argument expected for {shape_name}. Actual: {count}")
            c = Circle()
            c.set_radius(shape_data[0])
            return c
        else:
            raise ValueError("Shape Factory can only create 'circle', 'square', 'rectangle', and 'triangle'")
