import unittest
from Day3Part2 import *

class TestDay3Part1(unittest.TestCase):

    def test_checkCompartmentAssignment(self):
        data = ["vJrwpWtwJgWrhcsFMMfFFhFp\n", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n", "PmmdzqPrVvPwwTWBwg\n"]
        groupsack = GroupSack(data)
        self.assertEqual("vJrwpWtwJgWrhcsFMMfFFhFp", groupsack.backpackAList)
        self.assertEqual("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", groupsack.backpackBList)
        self.assertEqual("PmmdzqPrVvPwwTWBwg", groupsack.backpackCList)

    def test_checkCommonLetter(self):
        data = ["vJrwpWtwJgWrhcsFMMfFFhFp\n", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n", "PmmdzqPrVvPwwTWBwg\n"]
        groupsack = GroupSack(data)
        self.assertEqual("r", groupsack.commonLetter)

    def test_checkPointValue(self):
        data = ["vJrwpWtwJgWrhcsFMMfFFhFp\n", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n", "PmmdzqPrVvPwwTWBwg\n"]
        groupsack = GroupSack(data)
        self.assertEqual(18, groupsack.pointValue)

    def test_checkExampleCodeReturnsCorrectly(self):
        data = ["vJrwpWtwJgWrhcsFMMfFFhFp\n", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n", "PmmdzqPrVvPwwTWBwg\n", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n", 
        "ttgJtRGJQctTZtZT\n", "CrZsJsPPZsGzwwsLwLmpwMDw\n"]
        points = determineTotalPriorityValues(data)
        self.assertEqual(points, 70)


if __name__ == '__main__':
    unittest.main()