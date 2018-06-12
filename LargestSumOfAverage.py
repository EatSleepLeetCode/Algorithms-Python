class Solution:
    def largestSumOfAverages(self, A, K):
        n = len(A)
        cummulativeSum = [0] * (n + 1)

        for i in range(n):
            cummulativeSum[i + 1] = cummulativeSum[i] + A[i]

        def average(i, j):
            return (cummulativeSum[j] - cummulativeSum[i]) / float(j - i)

        dp = [average(i, n) for i in range(n)]

        for k in range(K - 1):
            for i in range(n):
                for j in range(i + 1, n):
                    dp[i] = max(dp[i], average(i, j) + dp[j])

        return dp[0]