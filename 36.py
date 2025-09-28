class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for index_of_sudoku_vertical in range(3):
            for index_of_sudoku in range(3):
                numbers = {}
                for i in range(3):
                    for j in range(3):
                        x = board[i+index_of_sudoku_vertical*3][j+index_of_sudoku*3]
                        if x != '.':
                            if x not in numbers:
                                numbers[x] = 1
                            else:
                                return False
                if numbers == {}:
                    return False
        return True


