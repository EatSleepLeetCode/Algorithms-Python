class Solution:
    def integerBreak(self, n):
        product = 1

        if n == 2:
            return 1
        if n == 3:
            return 2

        while n > 4:
            product *= 3
            n -= 3

        return product * n