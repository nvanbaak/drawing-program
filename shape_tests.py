import unittest

from shape import Shape


class MyShapeTests(unittest.TestCase):
    def test_init(self):
        shape = Shape()
        self.assertNotEqual(shape, None, "shape should not be None after construction")

    def test_automatic_fail(self):
        self.assertEqual(True, False, "You could have prevented this if you were a better coder")

if __name__ == '__main__':
    unittest.main()
