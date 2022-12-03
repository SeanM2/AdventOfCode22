import unittest
from Day3Part1 import *

class TestDay3Part1(unittest.TestCase):

    def test_checkCompartmentAssignment(self):
        data = "vJrwpWtwJgWrhcsFMMfFFhFp\n"
        backpack = Backpack(data)
        compartmentA = backpack.compartmentA
        compartmentB = backpack.compartmentB
        # print(compartmentA)
        # print(compartmentB)
        self.assertEqual(['v', 'J', 'r', 'w', 'p', 'W', 't', 'w', 'J', 'g', 'W', 'r'], compartmentA)
        self.assertEqual(["h","c","s","F","M","M","f","F","F","h","F","p"], compartmentB)

    def test_checkCommonLetter(self):
        data = "vJrwpWtwJgWrhcsFMMfFFhFp\n"
        backpack = Backpack(data)
        self.assertEqual("p", backpack.commonLetter)

    def test_checkPointValue(self):
        data = "vJrwpWtwJgWrhcsFMMfFFhFp\n"
        backpack = Backpack(data)
        self.assertEqual(16, backpack.pointValue)

    def test_checkExampleCodeReturnsCorrectly(self):
        data = ["vJrwpWtwJgWrhcsFMMfFFhFp\n", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n", "PmmdzqPrVvPwwTWBwg\n", 
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n", "ttgJtRGJQctTZtZT\n", "CrZsJsPPZsGzwwsLwLmpwMDw\n"]
        points = determineTotalPriorityValues(data)
        self.assertEqual(points, 157)


if __name__ == '__main__':
    unittest.main()