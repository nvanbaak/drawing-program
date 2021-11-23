# DrawingProgramMain creates a Drawing Program and adds shapes to it.
# Sorts the shapes, adds some more ahpes, replaces some shapes, sorts again.

from drawing_program import DrawingProgram
from shapefactory import ShapeFactory as sf
from square import Square
from circle import Circle
from triangle import Triangle
from rectangle import Rectangle

print("\nWelcome to Drawing Program!")
print("\nWe'll start by adding some shapes.  Here they are:")
my_drawing_program = DrawingProgram()

my_rectangle = sf.create_shape("rectangle", 2, 4.0)
my_square = sf.create_shape("square", 3.1)
my_triangle = sf.create_shape("triangle", 3, 4.0)
my_circle = sf.create_shape("circle", 3.1)

my_drawing_program.add_shape(my_square)
my_drawing_program.add_shape(my_circle)
my_drawing_program.add_shape(my_rectangle)
my_drawing_program.add_shape(my_triangle)
print(my_drawing_program)

print("Next, we'll sort the shapes by area: ")

my_drawing_program.sort_shapes()
print(my_drawing_program)

print("Let's add some more shapes: ")
my_drawing_program.add_shape(sf.create_shape("rectangle", 1, 2))
my_drawing_program.add_shape(sf.create_shape("square", 2))
my_drawing_program.add_shape(sf.create_shape("triangle", 1, 2))
my_drawing_program.add_shape(sf.create_shape("circle", 4))
print(my_drawing_program)

print("That's way too many shapes.  Let's remove a couple: ")
my_drawing_program.remove_shape(my_rectangle)
my_drawing_program.remove_shape(my_circle)
print(my_drawing_program)

print("You know what?  I don't like triangles.  Let's replace them with circles: ")
my_drawing_program.set_shape(0, sf.create_shape("circle", 4))
my_drawing_program.set_shape(4, sf.create_shape("circle", 2))
print(my_drawing_program)

print("Now they're all out of order.  Let's sort again: ")
my_drawing_program.sort_shapes()
print(my_drawing_program)