import unittest
from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle
from shapefactory import ShapeFactory

class ShapeFactoryTest(unittest.TestCase):

    def test_square_was_created(self):
        sq = Square()
        self.assertIsInstance(sq, Square, "Object expected to be a Square")

    def test_circle_was_created(self):
        c = Circle()
        self.assertIsInstance(c, Circle, "Object expected to be a Circle")

    def test_rectangle_was_created(self):
        r = Rectangle()
        self.assertIsInstance(r, Rectangle, "Object expected to be a Rectangle")

    def test_triangle_was_created(self):
        t = Triangle()
        self.assertIsInstance(t, Triangle, "Object expected to be a Triangle")

    def test_string_passed_as_square_arg(self):
        sq = Square()
        try:
            sq.set_side("two")
            self.assertEqual(True, False, "exception not thrown for square argument of string")
        except TypeError:
            self.assertEqual(True, True, "Square argument should be int or float")

    def test_string_passed_as_circle_arg(self):
        c = Circle()
        try:
            c.set_radius("two")
            self.assertEqual(True, False, "exception not thrown for circle argument of string")
        except TypeError:
            self.assertEqual(True, True, "Circle argument should be int or float")

    def test_string_passed_as_rectangle_arg(self):
        r = Rectangle()
        try:
            r.set_width("two")
            r.set_length("one")
            self.assertEqual(True, False, "exception not thrown for rectangle argument of string")
        except TypeError:
            self.assertEqual(True, True, "Rectangle arguments should be int or float")

    def test_string_passed_as_triangle_arg(self):
        t = Triangle()
        try:
            t.set_base("two")
            t.set_height("one")
            self.assertEqual(True, False, "exception not thrown for triangle argument of string")
        except TypeError:
            self.assertEqual(True, True, "Triangle arguments should be int or float")

    def test_shapefactory_passed_invalid_shape_name(self):
        try:
            my_shape = ShapeFactory.create_shape("circl", 3.1)
            self.assertEqual(True, False, "exception not thrown for invalid shape name")
        except ValueError:
            self.assertEqual(True, True, "Error: ShapeFactory can only create 'circle', 'square', 'rectangle' and 'triangle'")


if __name__ == '__main__':
    unittest.main()
