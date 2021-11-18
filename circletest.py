#code to test Circle class
import unittest

from circle import Circle

class CircleTest(unittest.TestCase):
    #This class tests the functionality provided by the Circle class

    def test_radius_negative_or_zero(self):
        #set radius to negative value which should raise an exception of ValueError
        another_circle = Circle()

        try:
            another_circle.set_radius(-1)
            self.assertEqual(True, False, "exception not thrown for length of side of -1")
        except ValueError:
            self.assertEqual(True, True)

        #set rdaius to zero value which should raise an exception of ValueError

        try:
            another_circle.set_radius(0)
            self.assertEqual(True, False, "exception not thrown for length of side of 0")
        except ValueError:
            self.assertEqual(True, True)


    def test_area_radius_3(self):
        #simple test to see if a positive length of side returns the correct area

        another_circle = Circle()
        another_circle.set_radius(3)
        self.assertEqual(28.27, round(another_circle.area(), 2), "area was not 28.27")

    def test_perimeter_side_length_3(self):
        #simple test to see if a positive length of side returns the correct perimeter

        another_circle = Circle()
        another_circle.set_radius(3)
        self.assertEqual(18.85, round(another_circle.perimeter(), 2), "perimeter/circumference was not 18.85")