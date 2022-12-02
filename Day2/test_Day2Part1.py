import unittest
from Day2Part1 import determineTotalPoints

class TestDay2Part1(unittest.TestCase):

    def test_checkOneValueIsCorrect(self):
        data = ["A X\n"]
        points = determineTotalPoints(data)
        self.assertEqual(points, 4)

    def test_checkExampleCodeReturnsCorrectly(self):
        data = ["A Y\n", "B X\n", "C Z\n"]
        points = determineTotalPoints(data)
        self.assertEqual(points, 15)


if __name__ == '__main__':
    unittest.main()