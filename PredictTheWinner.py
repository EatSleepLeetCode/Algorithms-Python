def PredictTheWinner(self, nums):
    n = len(nums)
    dp = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        dp[i][i] = nums[i]

    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

    return dp[0][n - 1] >= 0