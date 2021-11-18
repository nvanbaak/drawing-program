#code to test Rectangle class
import unittest
from rectangle import Rectangle

class RectangleTest(unittest.TestCase):
    #This class tests the functionality provided by the Rectangle class

    def test_rectangle_length_negative_or_zero(self):
        #set length of rectangle to negative value which should raise an exception of ValueError
        another_rectangle = Rectangle()

        try:
            another_rectangle.set_length(-1)
            self.assertEqual(True, False, "exception not thrown for length of rectangle of -1")
        except ValueError:
            self.assertEqual(True, True)

        #set length of rectangle to zero value which should raise an exception of ValueError

        try:
            another_rectangle.set_length(0)
            self.assertEqual(True, False, "exception not thrown for length of rectangle of 0")
        except ValueError:
            self.assertEqual(True, True)

    def test_rectangle_width_negative_or_zero(self):
        #set width of rectangle to negative value which should raise an exception of ValueError
        another_rectangle = Rectangle()

        try:
            another_rectangle.set_width(-1)
            self.assertEqual(True, False, "exception not thrown for width of rectangle of -1")
        except ValueError:
            self.assertEqual(True, True)

        #set width of rectangle to zero value which should raise an exception of ValueError

        try:
            another_rectangle.set_width(0)
            self.assertEqual(True, False, "exception not thrown for width of rectangle of 0")
        except ValueError:
            self.assertEqual(True, True)

    def test_area_rectangle_length_1_width_2(self):
        #simple test to see if a positive length and width of rectangle returns the correct area

        another_rectangle = Rectangle()
        another_rectangle.set_length(1)
        another_rectangle.set_width(2)
        self.assertEqual(2, round(another_rectangle.area(), 2), "area was not 2")

    def test_perimeter_rectangle_length_1_width_2(self):
        #simple test to see if a positive length and width of rectangle returns the correct perimeter

        another_rectangle = Rectangle()
        another_rectangle.set_length(1)
        another_rectangle.set_width(2)
        self.assertEqual(6, round(another_rectangle.perimeter(), 2), "perimeter was not 6")
