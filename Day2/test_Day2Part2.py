import unittest
from Day2Part2 import determineTotalPoints

class TestDay2Part1(unittest.TestCase):

    def test_checkOneValueIsCorrect(self):
        data = ["A Y\n"]
        points = determineTotalPoints(data)
        self.assertEqual(points, 4)

    def test_checkExampleCodeReturnsCorrectly(self):
        data = ["A Y\n", "B X\n", "C Z\n"]
        points = determineTotalPoints(data)
        self.assertEqual(points, 12)


if __name__ == '__main__':
    unittest.main()