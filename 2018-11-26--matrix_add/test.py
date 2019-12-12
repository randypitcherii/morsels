import unittest

from solution import add, add_multiple

class TestRunner(unittest.TestCase):
    def test_add1(self):
        matrix1 = [[1, -2], [-3, 4]]
        matrix2 = [[2, -1], [0, -1]]
        solution = [[3, -3], [-3, 3]]
        result = add(matrix1, matrix2)
        self.assertEqual(result, solution)

    def test_add2(self):
        matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
        matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
        result = add(matrix1, matrix2)
        solution = [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
        self.assertEqual(result, solution)

    def test_addMultiple1(self):
        matrix1 = [[1, -2], [-3, 4]]
        matrix2 = [[2, -1], [0, -1]]
        solution = [[3, -3], [-3, 3]]
        result = add_multiple(matrix1, matrix2)
        self.assertEqual(result, solution)

    def test_addMultiple2(self):
        matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
        matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
        result = add_multiple(matrix1, matrix2)
        solution = [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
        self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
