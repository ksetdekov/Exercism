import unittest


def done_or_not(board): #board[i][j]
    result = 'Try again!'
    test_rows = all([set(i) == {1, 2, 3, 4, 5, 6, 7, 8, 9} for i in board])
    test_columns = all([set([item[i] for item in board]) == {1, 2, 3, 4, 5, 6, 7, 8, 9} for i in range(9)])

    squares = []
    for i in [i*3 for i in range(3)]:
        for j in [j*3 for j in range(3)]:
            square = [row[j:j + 3] for row in board[i:i + 3]]
            square_check = set([item for sublist in square for item in sublist]) == {1, 2, 3, 4, 5, 6, 7, 8, 9}
            squares.append(square_check)
    squares_check = all(squares)
    if all([test_rows, test_columns, squares_check]):
        result = 'Finished!'

    return result


class TestingFunction(unittest.TestCase):
    def testCases(self):  # test method names begin with 'test'
        self.assertEqual(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]), 'Finished!')

    def testZero(self):  # test method names begin with 'test'
        self.assertEqual(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]), 'Try again!')


if __name__ == '__main__':
    unittest.main()
