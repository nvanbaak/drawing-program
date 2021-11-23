#code to test Triangle class
import unittest
from triangle import Triangle

class TriangleTest(unittest.TestCase):
    #This class tests the functionality provided by the Square class

    def test_base_length_negative_or_zero(self):
        #set base to negative value which should raise an exception of ValueError
        another_triangle = Triangle()

        try:
            another_triangle.set_base(-1)
            self.assertEqual(True, False, "exception not thrown for length of side of -1")
        except ValueError:
            self.assertEqual(True, True)

        #set base to zero value which should raise an exception of ValueError

        try:
            another_triangle.set_base(0)
            self.assertEqual(True, False, "exception not thrown for length of side of 0")
        except ValueError:
            self.assertEqual(True, True)

    def test_height_length_negative_or_zero(self):
        # set height to negative value which should raise an exception of ValueError
        another_triangle = Triangle()

        try:
            another_triangle.set_height(-1)
            self.assertEqual(True, False, "exception not thrown for base length of -1")
        except ValueError:
            self.assertEqual(True, True)

        # set base to zero value which should raise an exception of ValueError

        try:
            another_triangle.set_height(0)
            self.assertEqual(True, False, "exception not thrown for height length of 0")
        except ValueError:
            self.assertEqual(True, True)

    def test_area_triangle_base_1_height_1(self):
        #simple test to see if a positive base and height returns the correct area

        another_triangle = Triangle()
        another_triangle.set_base(1)
        another_triangle.set_height(1)
        self.assertEqual(0.5, round(another_triangle.area(), 2), "area was not 0.5")

    def test_perimeter_triangle_base_1_height_1(self):
        #simple test to see if a positive base and height returns the correct perimeter

        another_triangle = Triangle()
        another_triangle.set_base(1)
        another_triangle.set_height(1)
        self.assertEqual(3.24, round(another_triangle.perimeter(), 2), "perimeter was not 3.24")

if __name__ == "__main__":
    unittest.main()