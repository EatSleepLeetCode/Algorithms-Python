class Solution:
    def flipAndInvertImage1(self, A):
        n = len(A)

        for row in range(n):
            for col in range(int((n + 1) / 2)):
                A[row][col], A[row][n - 1 - col] = A[row][n - 1 - col] ^ 1, A[row][col] ^ 1

        return A

    def flipAndInvertImage(self, A):

        for row in A:
            for i in xrange((len(row) + 1) / 2):
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A
