import unittest
from Day9 import *


class TestDay9(unittest.TestCase):
    def test_checkDetermineTailPosition_1(self):
        headPosition = [1, 0]
        tailPosition = [0, 0]
        output = DetermineTailPosition(headPosition, tailPosition)
        # print(len(output))
        self.assertEqual(output, [0, 0])

    def test_checkDetermineTailPosition_2(self):
        headPosition = [1, 1]
        tailPosition = [0, 0]
        output = DetermineTailPosition(headPosition, tailPosition)
        # print(len(output))
        self.assertEqual(output, [0, 0])

    def test_checkDetermineTailPosition_3(self):
        headPosition = [2, 0]
        tailPosition = [0, 0]
        output = DetermineTailPosition(headPosition, tailPosition)
        # print(len(output))
        self.assertEqual(output, [1, 0])

    def test_checkDetermineTailPosition_4(self):
        headPosition = [2, 1]
        tailPosition = [0, 0]
        output = DetermineTailPosition(headPosition, tailPosition)
        # print(len(output))
        self.assertEqual(output, [1, 1])

    def test_checkDetermineTailPosition_5(self):
        headPosition = [-2, 0]
        tailPosition = [0, 0]
        output = DetermineTailPosition(headPosition, tailPosition)
        # print(len(output))
        self.assertEqual(output, [-1, 0])

    def test_checkDetermineTailPosition_6(self):
        headPosition = [-2, -1]
        tailPosition = [0, 0]
        output = DetermineTailPosition(headPosition, tailPosition)
        # print(len(output))
        self.assertEqual(output, [-1, -1])

    def test_checkProcessActionFile(self):
        with open("testData.txt", "r") as file:
            data = file.readlines()
        countOfPositions = ProcessActionFile(data)
        # print(len(output))
        self.assertEqual(countOfPositions, 36)


if __name__ == "__main__":
    unittest.main()
