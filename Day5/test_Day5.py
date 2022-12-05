import unittest
from Day5 import *

class TestDay5(unittest.TestCase):

    def test_checkCreateArrays(self):
        with open('input.txt', 'r') as file:
            fileOutput = file.readlines()
        data = fileOutput[0:8]
        output = CreateArrays(data)
        self.assertEqual(['R','N','F','V','L','J','S','M'], output[0])
        self.assertEqual(['N','B','S'], output[3])

    def test_checkDetermineInstructions(self):
        data = "move 1 from 2 to 1"
        moveTarget, originalIndex, newIndex = DetermineInstruction(data)
        self.assertEqual(moveTarget, 1)
        self.assertEqual(originalIndex, 1)
        self.assertEqual(newIndex, 0)

    def test_checkMoveTheCrates9000(self):
        with open('input.txt', 'r') as file:
            fileOutput = file.readlines()
        data = fileOutput[0:8]
        array = CreateArrays(data)
        instructionString = "move 1 from 1 to 4"
        moveTarget, originalIndex, newIndex = DetermineInstruction(instructionString)
        output = MoveTheCrates9000(array, moveTarget, originalIndex, newIndex)
        self.assertEqual(['R','N','F','V','L','J','S'], output[0])
        self.assertEqual(['N','B','S','M'], output[3])

    def test_checkMoveTheCrates9001(self):
        with open('input.txt', 'r') as file:
            fileOutput = file.readlines()
        data = fileOutput[0:8]
        array = CreateArrays(data)
        instructionString = "move 2 from 1 to 4"
        moveTarget, originalIndex, newIndex = DetermineInstruction(instructionString)
        output = MoveTheCrates9001(array, moveTarget, originalIndex, newIndex)
        self.assertEqual(['R','N','F','V','L','J'], output[0])
        self.assertEqual(['N','B','S','S','M'], output[3])

if __name__ == '__main__':
    unittest.main()