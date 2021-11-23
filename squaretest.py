#code to test Square class
import unittest
from square import Square

class SquareTest(unittest.TestCase):
    #This class tests the functionality provided by the Square class

    def test_invalid_side_length(self):
        another_square = Square()

        # Square should raise a ValueError for either of these values
        self.assertRaises(
                ValueError,
                another_square.set_side, -1)
        self.assertRaises(
                ValueError,
                another_square.set_side, 0)

    def test_area(self):
        #simple test to see if a positive length of side returns the correct area

        another_square = Square()
        another_square.set_side(3.1)
        self.assertEqual(9.61, round(another_square.area(), 2), "area was not 9.61")

    def test_perimeter(self):
        #simple test to see if a positive length of side returns the correct perimeter

        another_square = Square()
        another_square.set_side(3.1)
        self.assertEqual(12.4, round(another_square.perimeter(), 2), "perimeter was not 12.4")

if __name__ == "__main__":
    unittest.main()