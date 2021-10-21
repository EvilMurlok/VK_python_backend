import unittest
from my_metaclass import *


class TestMyMetaclass(unittest.TestCase):
    def test_class_point(self):
        self.point = CustomPointClass(228, 322)
        self.assertEqual(self.point.custom_x, 228)
        self.assertEqual(self.point.custom_y, 322)
        self.assertEqual(self.point.custom_coordinate_system, 'Cartesian')
        self.assertEqual(self.point.custom_dimension, 2)
        self.point.custom_set_new_point(-12345, 12345)
        self.assertEqual(self.point.custom_x, -12345)
        self.assertEqual(self.point.custom_y, 12345)
        with self.assertRaises(AttributeError):
            print(self.point.x)
        with self.assertRaises(AttributeError):
            print(self.point.y)
        with self.assertRaises(AttributeError):
            print(self.point.coordinate_system)
        with self.assertRaises(AttributeError):
            print(self.point.dimension)
        with self.assertRaises(AttributeError):
            self.point.set_new_point(666, 666)

    def test_example_class(self):
        self.example = CustomExampleClass(111)
        self.assertEqual(self.example.custom_x, 50)
        self.assertEqual(self.example.custom_val, 111)
        self.assertEqual(CustomExampleClass.custom_line(), 100)
        with self.assertRaises(AttributeError):
            print(self.example.x)
        with self.assertRaises(AttributeError):
            print(self.example.val)
        with self.assertRaises(AttributeError):
            print(CustomExampleClass.line())
