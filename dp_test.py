# nvb / 17 Nov 2021
# unit tests for Drawing Program

import unittest
from drawing_program import DrawingProgram as dp
from circle import Circle
from shapefactory_tests import MyShapeFactoryTests

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
            new_shape = Circle(radius)
            shape_list.append(new_shape)
        try:
            myDP = dp(shape_list)
            self.assertIsInstance(myDP, dp, "DrawingProgram failed to initialize with list of Shapes as parameter!")
        except:
            self.assertTrue(False, "Exception raised during initialization with shape_list parameter!")

    def test_init_fails_nonshapes(self):
        bad_list = [Circle(0), Circle(1), Circle(3), "12345"]
        try:
            myDP = dp(bad_list)
            self.assertTrue(False, "DrawingProgram initialized with bad parameters!")
        except TypeError:
            self.assertTrue(True)

    def test_add_shape(self):
        myDP = dp()
        test_circle = Circle(0)
        try:
            myDP.addShape(test_circle)
            self.assertEqual(myDP.shape_list[0], test_circle)
        except:
            self.assertTrue(False, "Exception raised during addShape()!")

    def test_str_empty(self):
        myDP = dp()
        self.assertEqual(myDP.__str__(), "", "__str__() of empty DrawingProgram failed to return an empty string!")
        pass

    def test_str_not_empty(self):
        myDP = dp()
        test_circle = Circle(0)
        myDP.addShape(test_circle)

        self.assertEqual(myDP.__str__(), test_circle.__str__(), "__str__() of DrawingProgram not equal to __str__() of contained shapes!")

    def test_add_non_shape(self):
        myDP = dp()
        self.assertRaises(TypeError, myDP.addShape, "12345")

    def test_get_shape(self):
        test_circle = Circle(3)
        myDP = dp([Circle(0), test_circle, Circle(5)])
        self.assertEqual(myDP.get_shape(1), test_circle, "get_shape() failed to return shape at correct index!")

    def test_get_shape_bad_index(self):
        myDP = dp([Circle(0), Circle(3), Circle(5)])
        self.assertRaises(IndexError, myDP.get_shape, 5)
        self.assertRaises(IndexError, myDP.get_shape, -1)

    def test_remove_shape(self):
        myDP = dp([Circle(0), Circle(1), Circle(2), Circle(3)])

        self.assertEqual(myDP.remove_shape(Circle(0)), 1, "remove_shape returns incorrect number of removals!")
        self.assertEqual(myDP.shape_list[0], Circle(1), "remove_shape failed to remove correct element!")
        self.assertEqual(len(myDP.shape_list), 3, "remove_shape failed to remove the correct number of elements!")

    def test_remove_shape_multiple(self):
        myDP = dp([Circle(0), Circle(0), Circle(0), Circle(3)])

        self.assertEqual(myDP.remove_shape(Circle(0)), 3, "remove_shape returns incorrect number of removals!")
        self.assertEqual(myDP.shape_list[0], Circle(3), "remove_shape failed to remove correct elements!")
        self.assertEqual(len(myDP.shape_list), 1, "remove_shape failed to remove the correct number of elements!")

    def test_remove_shape_absent(self):
        myDP = dp([Circle(0), Circle(1), Circle(2)])

        self.assertEqual(myDP.remove_shape(Circle(5)), 0, "remove_shape() reports removing elements where none should have been removed!")
        self.assertEqual(len(myDP.shape_list), 3, "remove_shape removed elements where there were no matches!")

    def test_remove_shape_nonshape(self):
        myDP = dp()
        self.assertRaises(TypeError, myDP.remove_shape, "not a shape")

    def test_sort_shapes(self):
        unsorted_shapes = [
            Circle(5),
            Circle(1),
            Circle(4),
            Circle(2),
            Circle(0),
            Circle(3)
            ]

        sorted_shapes = []
        for radius in range(0,6):
            sorted_shapes.append(Circle(radius))

        sorted_dp = dp(sorted_shapes)
        unsorted_dp = dp(unsorted_shapes)
        unsorted_dp.sort_shapes()

        self.assertEqual(sorted_dp.__str__(), unsorted_dp.__str__(), "List failed to sort properly!")

    def test_set_shape(self):
        myDP = dp([Circle(0), Circle(1), Circle(2), Circle(3)])
        myDP.set_shape(0, Circle(10))

        self.assertEqual(myDP.shape_list[0], Circle(10), "set_shape() did not change shape at specified index!")

    def test_set_shape_bad_index(self):
        myDP = dp([Circle(0), Circle(1), Circle(2), Circle(3)])

        self.assertRaises(IndexError, myDP.set_shape, index=-1, shape=Circle(10))
        self.assertRaises(IndexError, myDP.set_shape, index=6, shape=Circle(10))

    def test_set_shape_nonshape(self):
        myDP = dp([Circle(0), Circle(1), Circle(2), Circle(3)])

        self.assertRaises(TypeError, myDP.set_shape, index=0, shape="bwa ha ha, not a shape!")


if __name__ == "__main__":
    unittest.main()