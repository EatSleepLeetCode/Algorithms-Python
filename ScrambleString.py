class Solution:

    def isScramble(self, s1, s2):
        freq = [0] * 26

        if s1 == s2:
            return True

        for i in range(len(s1)):
            freq[ord(s1[i]) - ord('a')] += 1
            freq[ord(s2[i]) - ord('a')] -= 1

        for i in range(26):
            if freq[i] != 0:
                return False

        for i in range(1, len(s1)):
            if self.isScramble(s1[: i], s2[: i]) and self.isScramble(s1[i :], s2[i :]):
                return True
            if self.isScramble(s1[: i], s2[-i :]) and self.isScramble(s1[i :], s2[: -i]):
                return True
        return False

    # def __init__main(self):
    #     print(self.isScramble("great", "rgeat"))


solObj = Solution()
print(solObj.isScramble("great", "rgeat"))
print(solObj.isScramble("abcde", "caebd"))