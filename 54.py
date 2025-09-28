class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        result = []
        i, j = 0, 0

        up, down, left, right = 0, 1, 2, 3
        RIGHT_WALL, DOWN_WALL, LEFT_WALL, UP_WALL = n, m, -1, 0
        direction = right
        while len(result) < m * n:
            if direction == right:
                while j < RIGHT_WALL:
                    result.append(matrix[i][j])
                    j+=1
                RIGHT_WALL -=1
                i, j = i + 1, j - 1
                direction = down
            elif direction == down:
                while i < DOWN_WALL:
                    result.append(matrix[i][j])
                    i+=1
                DOWN_WALL -= 1
                i, j = i-1, j - 1
                direction = left
            elif direction == left:
                while j > LEFT_WALL:
                    result.append(matrix[i][j])
                    j-=1
                LEFT_WALL += 1
                i, j = i-1, j + 1
                direction = up
            elif direction == up:
                while i > UP_WALL:
                    result.append(matrix[i][j])
                    i-=1
                UP_WALL += 1
                i, j = i+1, j + 1
                direction = right
        return result