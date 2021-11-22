# DrawingProgramMain creates a Drawing Program and adds shapes to it.
# Sorts the shapes, adds some more ahpes, replaces some shapes, sorts again.

from drawing_program import DrawingProgram
from shapefactory import ShapeFactory
from square import Square
from circle import Circle
from triangle import Triangle
from rectangle import Rectangle

print("Create a class called DrawingProgramMain that creates a DrawingProgram.")
my_drawing_program = DrawingProgram()
print("Add shapes to it: ")

my_rectangle = ShapeFactory.create_shape("rectangle", 2, 4.0)

my_square = ShapeFactory.create_shape("square", 3.1)

my_triangle = ShapeFactory.create_shape("triangle", 3, 4.0)

my_circle = ShapeFactory.create_shape("circle", 3.1)

my_drawing_program.addShape(my_square)
my_drawing_program.addShape(my_circle)
my_drawing_program.addShape(my_rectangle)
my_drawing_program.addShape(my_triangle)
print(my_drawing_program)

print("Sort the shapes by area: ")
my_drawing_program.sort_shapes()
print(my_drawing_program)

print("Add more shapes: ")

my_rectangle = ShapeFactory.create_shape("rectangle", 1, 2)

my_square = ShapeFactory.create_shape("square", 2)

my_triangle = ShapeFactory.create_shape("triangle", 1, 2)

my_circle = ShapeFactory.create_shape("circle", 4)

my_drawing_program.addShape(my_triangle)
my_drawing_program.addShape(my_rectangle)
my_drawing_program.addShape(my_square)
my_drawing_program.addShape(my_circle)
print(my_drawing_program)

print("Replace some shapes: ")
my_drawing_program.remove_shape(my_circle)
another_circle = ShapeFactory.create_shape("circle", 4)
my_drawing_program.addShape(another_circle)
print(my_drawing_program)

print("Sort shapes again by area: ")
my_drawing_program.sort_shapes()
print(my_drawing_program)
