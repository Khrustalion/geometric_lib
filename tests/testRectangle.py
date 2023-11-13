import sys
sys.path.append(r"C:\Users\user\Documents\IS-1_semestr\1-semester\DevTools\lab2\geometric_lib")
import rectangle
import unittest


class RectangleTestCaseArea(unittest.TestCase):
    def testInvalidArgument(self):
        self.assertEqual(type(rectangle.area(-1, -2)), Exception)

    def testSimpleSides(self):
        self.assertEqual(rectangle.area(11, 20), 220)

    def testZeroSides(self):
        self.assertEqual(rectangle.area(0, 0), 0)

    def testZeroSide(self):
        self.assertEqual(rectangle.area(0, 100), 0)

    def testBigSides(self):
        self.assertEqual(rectangle.area(10_000, 12345), 123_450_000)


class RectangleTestCasePerimeter(unittest.TestCase):
    def testInvalidArgument(self):
        self.assertEqual(type(rectangle.perimeter(-1, -2)), Exception)

    def testSimpleSides(self):
        self.assertEqual(rectangle.perimeter(13, 14), 54)

    def testZeroSide(self):
        self.assertEqual(rectangle.perimeter(0, 20), 20)

    def testZeroSides(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def testPerimeterBigSides(self):
        self.assertEqual(rectangle.perimeter(10_001, 33_333), 86_668)