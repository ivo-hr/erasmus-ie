import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_init(self):
        rectangle = Rectangle(5, 3)
        self.assertEqual(rectangle.get_length(), 5)
        self.assertEqual(rectangle.get_width(), 3)

    def test_set_length(self):
        rectangle = Rectangle(5, 3)
        rectangle.set_length(7)
        self.assertEqual(rectangle.get_length(), 7)

    def test_set_width(self):
        rectangle = Rectangle(5, 3)
        rectangle.set_width(4)
        self.assertEqual(rectangle.get_width(), 4)

    def test_reset(self):
        rectangle = Rectangle(5, 3)
        rectangle.reset()
        self.assertEqual(rectangle.get_length(), 0)
        self.assertEqual(rectangle.get_width(), 0)

    def test_set_length_and_width(self):
        rectangle = Rectangle()
        rectangle.set_length_and_width(5, 3)
        self.assertEqual(rectangle.get_length(), 5)
        self.assertEqual(rectangle.get_width(), 3)

    def test_get_area(self):
        rectangle = Rectangle(5, 3)
        self.assertEqual(rectangle.get_area(), 15)

    def test_get_side_ratio(self):
        rectangle = Rectangle(5, 3)
        self.assertEqual(rectangle.get_side_ratio(), 5/3)

    def test_get_is_square(self):
        rectangle = Rectangle(5, 5)
        self.assertTrue(rectangle.get_is_square())
        rectangle.set_width(3)
        self.assertFalse(rectangle.get_is_square())

    def test_rotate(self):
        rectangle = Rectangle(5, 3)
        rectangle.rotate()
        self.assertEqual(rectangle.get_length(), 3)
        self.assertEqual(rectangle.get_width(), 5)

if __name__ == '__main__':
    unittest.main()
