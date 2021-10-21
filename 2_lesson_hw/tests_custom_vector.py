import unittest
from custom_vector import *


# [9, 8, 7, 6, 5, 4, 3, 2, 1] vc
# [1, 2, 3, 4, 5] vc
# [] vc
# [0, 1, 2, 3, 4, 5, 6] list


class TestCustomVector(unittest.TestCase):
    def setUp(self) -> None:
        self.cv1 = CustomNumericalList(list(range(9, 0, -1)))
        self.cv2 = CustomNumericalList(list(range(1, 6)))
        self.cv3 = CustomNumericalList([])
        self.cv4 = list(range(7))

    def test_add(self):
        self.assertEqual(self.cv1 + self.cv2, CustomNumericalList([10, 10, 10, 10, 10, 4, 3, 2, 1]))
        self.assertEqual(self.cv2 + self.cv1, CustomNumericalList([10, 10, 10, 10, 10, 4, 3, 2, 1]))
        self.assertEqual(self.cv1 + self.cv3, CustomNumericalList(list(range(9, 0, -1))))
        self.assertEqual(self.cv2 + self.cv4, CustomNumericalList([1, 3, 5, 7, 9, 5, 6]))
        self.assertEqual(self.cv3 + self.cv3, CustomNumericalList([]))
        self.assertEqual(self.cv4 + self.cv1, CustomNumericalList([9, 9, 9, 9, 9, 9, 9, 2, 1]))

    # [9, 8, 7, 6, 5, 4, 3, 2, 1] vc
    # [1, 2, 3, 4, 5] vc
    # [] vc
    # [0, 1, 2, 3, 4, 5, 6] list

    def test_sub(self):
        self.assertEqual(self.cv1 - self.cv2, CustomNumericalList([8, 6, 4, 2, 0, 4, 3, 2, 1]))
        self.assertEqual(self.cv2 - self.cv1, CustomNumericalList([-8, -6, -4, -2, 0, -4, -3, -2, -1]))
        self.assertEqual(self.cv1 - self.cv3, CustomNumericalList(list(range(9, 0, -1))))
        self.assertEqual(self.cv3 - self.cv1, CustomNumericalList(list(range(-9, 0))))
        self.assertEqual(self.cv2 - self.cv4, CustomNumericalList([1, 1, 1, 1, 1, -5, -6]))
        self.assertEqual(self.cv3 - self.cv3, CustomNumericalList([]))
        self.assertEqual(self.cv4 - self.cv1, CustomNumericalList([-9, -7, -5, -3, -1, 1, 3, -2, -1]))

    def test_ge(self):
        self.assertEqual(self.cv1 >= self.cv2, True)
        self.assertEqual(self.cv2 >= self.cv1, False)
        self.assertEqual(self.cv1 >= self.cv3, True)
        self.assertEqual(self.cv3 >= self.cv1, False)
        self.assertEqual(self.cv2 >= self.cv4, False)
        self.assertEqual(self.cv3 >= self.cv3, True)
        self.assertEqual(self.cv4 >= self.cv1, False)

    def test_le(self):
        self.assertEqual(self.cv1 <= self.cv2, False)
        self.assertEqual(self.cv4 <= self.cv1, True)
        self.assertEqual(self.cv2 <= self.cv3, False)
        self.assertEqual(self.cv3 <= self.cv1, True)
        self.assertEqual(self.cv2 <= self.cv4, True)
        self.assertEqual(self.cv3 <= self.cv3, True)
        self.assertEqual(self.cv4 <= self.cv4, True)

    def test_gt(self):
        self.assertEqual(self.cv1 > self.cv2, True)
        self.assertEqual(self.cv2 > self.cv2, False)
        self.assertEqual(self.cv1 > self.cv1, False)
        self.assertEqual(self.cv3 > self.cv1, False)
        self.assertEqual(self.cv2 > self.cv4, False)
        self.assertEqual(self.cv3 > self.cv3, False)
        self.assertEqual(self.cv1 > self.cv4, True)

    def test_lt(self):
        self.assertEqual(self.cv1 < self.cv2, False)
        self.assertEqual(self.cv2 < self.cv2, False)
        self.assertEqual(self.cv1 < self.cv1, False)
        self.assertEqual(self.cv3 < self.cv1, True)
        self.assertEqual(self.cv2 < self.cv4, True)
        self.assertEqual(self.cv3 < self.cv3, False)
        self.assertEqual(self.cv1 < self.cv4, False)