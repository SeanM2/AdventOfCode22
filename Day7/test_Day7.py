import unittest
from Day7 import *


class TestDay6Part1(unittest.TestCase):
    def test_checkCreateDirectories(self):
        with open("testData.txt", "r") as file:
            data = file.readlines()
        output = CreateDirectories(data)
        for folder in output.listOfFolders:
            print(folder.name)
        print(output.listOfFolders)
        self.assertEqual(output.name, "/")
        self.assertEqual(output.GetFolderByName("d").name, "d")

    def test_checkFolderSizes(self):
        sumOfNumberBelow10000 = 0
        with open("testData.txt", "r") as file:
            data = file.readlines()
        output = CreateDirectories(data)
        output.GetFolderSizes()
        self.assertEqual(output.directorySize, 48381165)
        self.assertEqual(output.GetFolderByName("d").directorySize, 24933642)
        self.assertEqual(
            output.GetFolderByName("a").GetFolderByName("e").directorySize, 584
        )
        self.assertEqual(output.GetFolderByName("a").directorySize, 94853)


if __name__ == "__main__":
    unittest.main()
