# nvb / 17 Nov 2021
# unit tests for Drawing Program

import unittest
from drawing_program import DrawingProgram as dp
from shapefactory import ShapeFactory as sf

class MyDPTests(unittest.TestCase):
    """
    Unit tests for the DrawingProgram object
    """

    def test_init_no_param(self):
        my_dp = dp()
        self.assertIsInstance(my_dp, dp,
                "DrawingProgram failed to initialize with empty parameters!")

    def test_init_shape_list(self):
        shape_list = []        
        for radius in range(1,6):
            new_shape = sf.create_shape("circle", radius)
            shape_list.append(new_shape)
        try:
            my_dp = dp(shape_list)
            self.assertIsInstance(my_dp, dp,
                    "DrawingProgram failed to initialize with list of Shapes as parameter!")
        except:
            self.assertTrue(False,
                    "Exception raised during initialization with shape_list parameter!")

    def test_init_fails_nonshapes(self):
        bad_list = [
                sf.create_shape("circle",1),
                sf.create_shape("circle",2),
                sf.create_shape("circle",3),
                "12345"]
        try:
            my_dp = dp(bad_list)
            self.assertTrue(False,
                    "DrawingProgram initialized with bad parameters!")
        except TypeError:
            self.assertTrue(True)

    def test_add_shape(self):
        my_dp = dp()
        test_circle = sf.create_shape("circle",1)
        try:
            my_dp.add_shape(test_circle)
            self.assertEqual(my_dp.get_shape(0), test_circle)
        except:
            self.assertTrue(False,
                    "Exception raised during add_shape()!")

    def test_str_empty(self):
        self.assertEqual(
                dp().__str__(), "",
                "__str__() of empty DrawingProgram failed to return an empty string!")

    def test_str_not_empty(self):
        my_dp = dp()
        test_circle = sf.create_shape("circle",1)
        my_dp.add_shape(test_circle)

        self.assertEqual(
                my_dp.__str__(),
                test_circle.__str__()+ "\n",
                "__str__() of DrawingProgram not equal to __str__() of contained shapes!")

    def test_add_non_shape(self):
        my_dp = dp()
        self.assertRaises(TypeError, my_dp.add_shape, "12345")

    def test_get_shape(self):
        test_circle = sf.create_shape("circle",3)
        my_dp = dp([
                sf.create_shape("circle",1),
                test_circle,
                sf.create_shape("circle",5)])

        self.assertEqual(
                my_dp.get_shape(1),
                test_circle,
                "get_shape() failed to return shape at correct index!")

    def test_get_shape_bad_index(self):
        my_dp = dp([
                sf.create_shape("circle",1),
                sf.create_shape("circle",3),
                sf.create_shape("circle",5)])
        self.assertRaises(IndexError, my_dp.get_shape, 5)
        self.assertRaises(IndexError, my_dp.get_shape, -1)

    def test_remove_shape(self):
        my_dp = dp([
                sf.create_shape("circle",1),
                sf.create_shape("circle",2),
                sf.create_shape("circle",3),
                sf.create_shape("circle",4)])

        self.assertEqual(
                my_dp.remove_shape(sf.create_shape("circle",1)),
                1,
                "remove_shape returns incorrect number of removals!")
        self.assertEqual(
                my_dp.get_shape(0),
                sf.create_shape("circle",2),
                "remove_shape failed to remove correct element!")
        self.assertEqual(
                len(my_dp._DrawingProgram__shape_list),
                3,
                "remove_shape failed to remove the correct number of elements!")

    def test_remove_shape_multiple(self):
        my_dp = dp([
                sf.create_shape("circle",1),
                sf.create_shape("circle",1),
                sf.create_shape("circle",1),
                sf.create_shape("circle",3)])

        self.assertEqual(
                my_dp.remove_shape(sf.create_shape("circle",1)),
                3,
                "remove_shape returns incorrect number of removals!")
        self.assertEqual(
                my_dp.get_shape(0),
                sf.create_shape("circle",3),
                "remove_shape failed to remove correct elements!")
        self.assertEqual(
                len(my_dp._DrawingProgram__shape_list),
                1,
                "remove_shape failed to remove the correct number of elements!")

    def test_remove_shape_absent(self):
        my_dp = dp([
                sf.create_shape("circle",1),
                sf.create_shape("circle",2),
                sf.create_shape("circle",3)])

        self.assertEqual(
                my_dp.remove_shape(sf.create_shape("circle",5)),
                0,
                "remove_shape() reports removing elements where none should have been removed!")
        self.assertEqual(
                len(my_dp._DrawingProgram__shape_list),
                3,
                "remove_shape removed elements where there were no matches!")

    def test_sort_shapes(self):
        unsorted_shapes = [
                sf.create_shape("circle",5),
                sf.create_shape("circle",1),
                sf.create_shape("circle",4),
                sf.create_shape("circle",2),
                sf.create_shape("circle",6),
                sf.create_shape("circle",3)
                ]

        sorted_shapes = []
        for radius in range(1,7):
            sorted_shapes.append(sf.create_shape("circle",radius))

        sorted_dp = dp(sorted_shapes)
        unsorted_dp = dp(unsorted_shapes)
        unsorted_dp.sort_shapes()

        self.assertEqual(sorted_dp.__str__(), unsorted_dp.__str__(), "List failed to sort properly!")

    def test_set_shape(self):
        my_dp = dp([
                sf.create_shape("circle",1),
                sf.create_shape("circle",2),
                sf.create_shape("circle",3),
                sf.create_shape("circle",4)])
        my_dp.set_shape(0, sf.create_shape("circle",10))

        self.assertEqual(
                my_dp.get_shape(0),
                sf.create_shape("circle",10),
                "set_shape() did not change shape at specified index!")

    def test_set_shape_bad_index(self):
        my_dp = dp([
                sf.create_shape("circle",1),
                sf.create_shape("circle",2),
                sf.create_shape("circle",3),
                sf.create_shape("circle",4)])

        self.assertRaises(
                IndexError,
                my_dp.set_shape,
                index=-1,
                shape=sf.create_shape("circle",10))
        self.assertRaises(
                IndexError,
                my_dp.set_shape,
                index=6,
                shape=sf.create_shape("circle",10))

    def test_set_shape_nonshape(self):
        my_dp = dp([
                sf.create_shape("circle",1),
                sf.create_shape("circle",2),
                sf.create_shape("circle",3),
                sf.create_shape("circle",4)])

        self.assertRaises(
                TypeError,
                my_dp.set_shape,
                index=0,
                shape="bwa ha ha, not a shape!")

    def test_iteration(self):
        shapes = []
        for r in range(1,6):
            shapes.append(sf.create_shape("circle", r))

        my_dp = dp(shapes)

        # this logic is identical to dp.__str__, so they should be equal
        output = ""
        for shape in my_dp:
            output += shape.__str__() + "\n"

        self.assertEqual(output, my_dp.__str__())



if __name__ == "__main__":
    unittest.main()