class Solution:
    def findDiagonalOrder(self, matrix):
        rows = len(matrix)
        if rows == 0:
            return []
        cols = len(matrix[0])
        if cols == 0:
            return []

        result = [0] * rows * cols
        row, col, d = 0, 0, 1

        for i in range(rows * cols):
            result[i] = matrix[row][col]
            row -= d
            col += d

            if row >= rows:
                row = rows - 1
                col += 2
                d = -d

            if col >= cols:
                col = cols - 1
                row += 2
                d = -d

            if row < 0:
                row = 0
                d = -d

            if col < 0:
                col = 0
                d = -d

        return result