import unittest
from Day8 import *


class TestDay6Part1(unittest.TestCase):
    def test_checkCreateForest(self):
        with open("testData.txt", "r") as file:
            data = file.readlines()
        output = CreateForest(data)
        # print(len(output))
        self.assertEqual(output[0][0].height, 3)
        self.assertEqual(output[1][2].height, 5)
        self.assertEqual(output[4][3].height, 9)
        self.assertEqual(output[3][4].height, 9)
        self.assertEqual(output[0][0].visible, True)

    def test_checkCheckVisibilityToEdge(self):
        with open("testData.txt", "r") as file:
            data = file.readlines()
        forest = CreateForest(data)
        output = CheckVisibilityToEdge(forest, 1, 1)
        self.assertEqual(output, True)

    def test_checkDetermineVisibility(self):
        with open("testData.txt", "r") as file:
            data = file.readlines()
        forest = CreateForest(data)
        numberOfVisible, sceneryRating = DetermineForestVisibility(forest)
        self.assertEqual(numberOfVisible, 21)

    def test_checkDetermineTreeScenicRating(self):
        with open("testData.txt", "r") as file:
            data = file.readlines()
        forest = CreateForest(data)
        sceneryRating = DetermineTreeScenicRating(forest, 1, 2)
        self.assertEqual(sceneryRating, 4)


if __name__ == "__main__":
    unittest.main()
