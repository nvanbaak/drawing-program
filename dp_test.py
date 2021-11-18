# nvb / 17 Nov 2021
# unit tests for Drawing Program

import unittest
from drawing_program import DrawingProgram as dp
from circle import Circle

class MyDPTests(unittest.TestCase):
    """
    Unit tests for the DrawingProgram object
    """

    def test_init_no_param(self):
        myDP = dp()
        self.assertIsInstance(myDP, dp, "DrawingProgram failed to initialize with empty parameters!")

    def test_init_shape_list(self):
        shape_list = []        
        for radius in range(1,6):
            new_shape = Circle()
            new_shape.set_radius(radius)
            shape_list.append(new_shape)
        try:
            myDP = dp(shape_list)
            self.assertIsInstance(myDP, dp, "DrawingProgram failed to initialize with list of Shapes as parameter!")
        except:
            self.assertTrue(False, "Exception raised during initialization with shape_list parameter!")



    def test_str_empty(self):
        pass

    def test_str_not_empty(self):
        pass

    def test_add_shape(self):
        myDP = dp()
        myDP.addShape(Circle())

    def test_add_non_shape(self):
        pass

    def test_remove_shape(self):
        pass

    def test_remove_shape_multiple(self):
        pass

    def test_remove_shape_absent(self):
        pass

    def test_remove_shape_nonshape(self):
        pass

    def test_sort_shapes(self):
        pass

    def test_get_shape(self):
        pass

    def test_get_shape_bad_index(self):
        pass

    def test_set_shape(self):
        pass

    def test_set_shape_bad_index(self):
        pass

    def test_set_shape_nonshape(self):
        pass



if __name__ == "__main__":
    unittest.main()