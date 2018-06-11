import sys

class Solution:
    def maxDistToClosest(self, seats):
        n, result = len(seats), -sys.maxsize - 1
        left, right = [0] * n, [0] * n

        for i in range(n):
            if seats[i] == 1:
                left[i] = 0
            else:
                if i > 0:
                    left[i] = left[i - 1] + 1
                else:
                    left[i] = sys.maxsize

        for i in range(n - 1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            else:
                if i < n - 1:
                    right[i] = right[i + 1] + 1
                else:
                    right[i] = sys.maxsize

        return max(min(left[i], right[i]) for i, seat in enumerate(seats) if seat == 0)
