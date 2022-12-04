import unittest
from Day4Part2 import *

class TestDay3Part1(unittest.TestCase):

    def test_checkCompartmentAssignment(self):
        data = ["2-4,6-8\n", "2-3,4-5\n", "5-7,7-9\n", "2-8,3-7\n", "6-6,4-6\n", "2-6,4-8\n"]
        output = determineNumberOfContained(data)
        self.assertEqual(4, output)

if __name__ == '__main__':
    unittest.main()