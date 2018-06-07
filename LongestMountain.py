import sys

class Solution:

    def longestMountain1(self, A):
        n = len(A)
        up = [0 for _ in range(n)]
        down = [0 for _ in range(n)]
        result = -sys.maxsize - 1

        for i in range(n - 2, 0, -1):
            if A[i] > A[i + 1]:
                down[i] = down[i + 1] + 1

        for i in range(1, n):
            if A[i] > A[i - 1]:
                up[i] = up[i - 1] + 1

        for i in range(n):
            if up[i] > 0 and down[i] > 0:
                result = max(result, up[i] + down[i] + 1)

        result = result if result >= 3 else 0
        return result

    def longestMountain(self, A):
        n = len(A)
        up, down = 0, 0
        result = -sys.maxsize - 1

        for i in range(1, n):
            if (down > 0 and A[i - 1] < A[i]) or A[i - 1] == A[i]:
                up, down = 0, 0
            if A[i - 1] < A[i]:
                up += 1
            if A[i - 1] > A[i]:
                down += 1
            if up > 0 and down > 0:
                result = max(result, up + down + 1)

        result = result if result >= 3 else 0
        return result

obj = Solution()
print(obj.longestMountain1([2,1,4,7,3,2,5]))
print(obj.longestMountain([2,1,4,7,3,2,5]))