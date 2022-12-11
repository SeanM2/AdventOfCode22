import unittest
from Day10 import *


class TestDay9(unittest.TestCase):
    def test_checkTestData(self):
        with open("testData.txt", "r") as file:
            data = file.readlines()
        output = ProcessCpuInstructions(data)
        # print(len(output))
        self.assertEqual(output, 13140)


if __name__ == "__main__":
    unittest.main()
