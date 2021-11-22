# DrawingProgramMain creates a Drawing Program and adds shapes to it.
# Sorts the shapes, adds some more ahpes, replaces some shapes, sorts again.

from drawing_program import DrawingProgram
from square import Square
from circle import Circle
from triangle import Triangle
from rectangle import Rectangle

print("Create a class called DrawingProgramMain that creates a DrawingProgram.")
my_drawing_program = DrawingProgram()
print("Add shapes to it: ")
my_square = Square()
my_square.set_side(10)
my_circle = Circle()
my_circle.set_radius(1)
another_circle = Circle()
another_circle.set_radius(2)
my_drawing_program.addShape(my_square)
my_drawing_program.addShape(my_circle)
my_drawing_program.addShape(another_circle)
print(my_drawing_program)
print("Sort the shapes: ")
my_drawing_program.sort_shapes()
print(my_drawing_program)

print("Add more shapes: ")
my_triangle = Triangle()
my_triangle.set_height(3)
my_triangle.set_base(4)
my_rectangle = Rectangle()
my_rectangle.set_width(2)
my_rectangle.set_length(4)
my_drawing_program.addShape(my_triangle)
my_drawing_program.addShape(my_rectangle)
print(my_drawing_program)

print("Replace some shapes: ")
my_drawing_program.remove_shape(my_circle)
my_drawing_program.addShape(another_circle)
print(my_drawing_program)

print("Sort shapes again: ")
my_drawing_program.sort_shapes()
print(my_drawing_program)
