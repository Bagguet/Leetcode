class Solution(object):
    def rotate(self, matrix):
        """
        transpose the matrix and then reverse rows to get 90 deg rotation
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i].reverse()
        return matrix
