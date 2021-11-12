#code to test Square class
import unittest
from square import Square

class SquareTest(unittest.TestCase):
    #This class tests the functionality provided by the Square class

    #def test_init_default_and_str(self):
    #Tests to see the default values?

    def test_side_length_negative_or_zero(self):
        #set length_of_side to negative value which should raise an exception of ValueError
        mysquare = Square()
        self.__length_of_side = -1
        try:
            mysquare.set_side(-1)
            self.assertEqual(True, False, "exception not thrown for length of side of -1")
        except ValueError:
            self.assertEqual(True, True)

        self.__length_of_side = 0
        try:
            mysquare.set_side(0)
            self.assertEqual(True, False, "exception not thrown for length of side of 0")
        except ValueError:
            self.assertEqual(True, True)




    def test_area_side_length_3point1(self):
        #simple test to see if a positive length of side returns the correct area

        mysquare = Square()
        mysquare.set_side(3.1)
        self.assertEqual(9.61, round(mysquare.area(), 2), "area was not 9.61")

    def test_perimeter_side_length_3point1(self):
        #simple test to see if a positive length of side returns the correct perimeter

        mysquare = Square()
        mysquare.set_side(3.1)
        self.assertEqual(12.4, round(mysquare.perimeter(), 2), "perimeter was not 12.4")

