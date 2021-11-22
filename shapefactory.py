from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle

class ShapeFactory:
    """ It will be responsible for creating shapes. Anything that wants a shape *should* do it through the ShapeFactory.
    This class will have a method (or methods if you want) to create appropriate shapes."""

    # For the intents and purposes of this assignment, all shapes should be created via ShapeFactory.
    # Thus any adding of shapes to your DrawingProgram class object must be done through ShapeFactory.
    # This may seem cumbersome, but the point is to leave object creation to a single class.
    # It encapsulates how to create the objects you need.
    # make sure it creates and returns all 4 shapes
    # As part of testing one item, you will necessarily test other items. This is perfectly fine for our intents and
    # purposes. Just be sure an document what is being tested.

    @staticmethod
    def create_shape(shape_name, *args):
        shape_data = []
        count = 0
        for arg in args:
            shape_data.append(arg)
            count = count + 1
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

    # creates a shape of the specified type using the necessary data for building that shape
        # and returns that shape
        # e.g.: my_shape = ShapeFactory.create_shape("Circle", 2.0), where 2.0 is the radius of
        # the circle
        # e.g.: my_shape = ShapeFactory.create_shape("Rectangle", 2.0, 4.0), where 2.0 is length
        # and 4.0 is width
        # place the @staticmethod decorator/annotation on top of your create_shape definition to
        # allow you to call it as shown in above examples
        # NOTE: If you would like, you can instead have individual create methods for circle,
        # square, triangle, and rectangle. This will get rid of the need for a big nested if else
        # inside create_shape. Thus you could have create_circle, create_square, etc.

my_shape = ShapeFactory.create_shape("rectangle", 2, 4.0)
print(my_shape)
my_shape = ShapeFactory.create_shape("square", 3.1)
print(my_shape)
my_shape = ShapeFactory.create_shape("triangle", 3, 4.0)
print(my_shape)
my_shape = ShapeFactory.create_shape("circle", 3.1)
print(my_shape)
