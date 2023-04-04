import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertIn(solution([1,2,3,4,5,6,7,8,9,10], 11), [[0, 9], [9, 0]])

    def test_2(self):
        self.assertIn(solution([1,54,21,34,16], 17), [[4, 0], [0, 4]])

    def test_3(self):
        self.assertEqual(solution([1,2,3,4,5,6,7,8,9,10], 999), [-1, -1])

if __name__ == '__main__':
    unittest.main()