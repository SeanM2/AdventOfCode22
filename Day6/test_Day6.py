import unittest
from Day6 import *

class TestDay6Part1(unittest.TestCase):

    def test_checkDetermineMarkerPosition_1(self):
        data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
        output = DetermineMarkerPositionPart1(data)
        self.assertEqual(5, output)

    def test_checkDetermineMarkerPosition_2(self):
        data = "nppdvjthqldpwncqszvftbrmjlhg"
        output = DetermineMarkerPositionPart1(data)
        self.assertEqual(6, output)

    def test_checkDetermineMarkerPosition_3(self):
        data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
        output = DetermineMarkerPositionPart1(data)
        self.assertEqual(10, output)

    def test_checkDetermineMarkerPosition_4(self):
        data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
        output = DetermineMarkerPositionPart1(data)
        self.assertEqual(11, output)

    def test_checkDetermineMarkerPosition_1(self):
        data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
        output = DetermineMarkerPositionPart2(data)
        self.assertEqual(19, output)

    def test_checkDetermineMarkerPosition_2(self):
        data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
        output = DetermineMarkerPositionPart2(data)
        self.assertEqual(23, output)

    def test_checkDetermineMarkerPosition_3(self):
        data = "nppdvjthqldpwncqszvftbrmjlhg"
        output = DetermineMarkerPositionPart2(data)
        self.assertEqual(23, output)

    def test_checkDetermineMarkerPosition_4(self):
        data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
        output = DetermineMarkerPositionPart2(data)
        self.assertEqual(29, output)

    def test_checkDetermineMarkerPosition_5(self):
        data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
        output = DetermineMarkerPositionPart2(data)
        self.assertEqual(26, output)

if __name__ == '__main__':
    unittest.main()