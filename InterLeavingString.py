class Solution:
    def isInterleave(self, s1, s2, s3):
        s1Len = len(s1)
        s2Len = len(s2)
        s3Len = len(s3)

        if s1Len + s2Len != s3Len:
            return False

        foo = False
        dp = [[foo for x in range(s2Len + 1)] for y in range(s1Len + 1)]

        for i in range(s1Len + 1):
            for j in range(s2Len + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]  # compare s2
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]  # compare s1
                else:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1] or \
                               dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
        return dp[s1Len][s2Len]


obj = Solution()
print(obj.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(obj.isInterleave("aabcc", "dbbca", "aadbbbaccc"))