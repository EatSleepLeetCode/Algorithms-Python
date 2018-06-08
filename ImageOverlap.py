class Solution:
    def largestOverlap(self, A, B):
        result, n = 0, len(A)
        count = [[0 for x in range(2 * n + 1)] for y in range(2 * n + 1)]

        for iA in range(n):
            for jA in range(n):
                if A[iA][jA] is not 1:
                    continue
                for iB in range(n):
                    for jB in range(n):
                        if B[iB][jB] is not 1:
                            continue
                        count[iA - iB + n][jA - jB + n] += 1

        for row in count:
            for val in row:
                result = max(result, val)

        return result


