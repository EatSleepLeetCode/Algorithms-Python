class Solution:
    def minCut(self, s):

        n = len(s)
        foo = 0
        minCut = [foo for x in range(n)]

        for i in range(n):
            minCut[i] = i

        for i in range(n):
            self.palindromeSearch(s, minCut, i, i)
            self.palindromeSearch(s, minCut, i, i + 1)

        return minCut[n - 1]

    def palindromeSearch(self, s, minCut, left, right):
        n = len(s)
        while left >= 0 and right < n:
            if s[left] != s[right]:
                return

            if left == 0:
                minCut[right] = 0
            else:
                minCut[right] = min(minCut[right], minCut[left - 1] + 1)

            left -= 1
            right += 1

obj = Solution()
print(obj.minCut("aab"))