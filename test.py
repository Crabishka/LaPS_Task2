import unittest

from main import delete_empties, delete_empties_not_func_style


class Test(unittest.TestCase):

    def test_casual_case_1_func(self):
        test_matrix = [[1, 2, 3, 0],
                       [0, 0, 0, 0],
                       [3, 4, 5, 0],
                       [0, 1, 2, 0]]
        self.assertEqual(delete_empties(test_matrix), [[1, 2, 3],
                                                       [3, 4, 5],
                                                       [0, 1, 2]])

    def test_casual_case_1(self):
        test_matrix = [[1, 2, 3, 0],
                       [0, 0, 0, 0],
                       [3, 4, 5, 0],
                       [0, 1, 2, 0]]
        self.assertEqual(delete_empties_not_func_style(test_matrix), [[1, 2, 3],
                                                                      [3, 4, 5],
                                                                      [0, 1, 2]])

    def test_casual_case_2_func(self):
        test_matrix = [[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12],
                       [13, 14, 15, 16]]
        self.assertEqual(delete_empties(test_matrix), [[1, 2, 3, 4],
                                                       [5, 6, 7, 8],
                                                       [9, 10, 11, 12],
                                                       [13, 14, 15, 16]])

    def test_casual_case_2(self):
        test_matrix = [[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12],
                       [13, 14, 15, 16]]
        self.assertEqual(delete_empties_not_func_style(test_matrix),
                         [[1, 2, 3, 4],
                          [5, 6, 7, 8],
                          [9, 10, 11, 12],
                          [13, 14, 15, 16]])

    def test_casual_case_3_func(self):
        test_matrix = [[0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]]
        self.assertEqual(delete_empties(test_matrix), [])

    def test_casual_case_3(self):
        test_matrix = [[0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]]
        self.assertEqual(delete_empties_not_func_style(test_matrix), [])

    def test_casual_case_4_func(self):
        test_matrix = []
        self.assertEqual(delete_empties(test_matrix), [])

    def test_casual_case_4(self):
        test_matrix = []
        self.assertEqual(delete_empties_not_func_style(test_matrix), [])

    def test_casual_case_5_func(self):
        test_matrix = [[1, 0, 3, 0],
                       [0, 0, 0, 0],
                       [3, 0, 5, 0],
                       [0, 0, 2, 0]]
        self.assertEqual(delete_empties(test_matrix), [[1, 3],
                                                       [3, 5],
                                                       [0, 2]])

    def test_casual_case_5(self):
        test_matrix = [[1, 0, 3, 0],
                       [0, 0, 0, 0],
                       [3, 0, 5, 0],
                       [0, 0, 2, 0]]
        self.assertEqual(delete_empties_not_func_style(test_matrix), [[1, 3],
                                                                      [3, 5],
                                                                      [0, 2]])
