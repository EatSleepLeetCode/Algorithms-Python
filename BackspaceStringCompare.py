class Solution:

    def backspaceCompare(self, S, T):
        return self.parseString(S) == self.parseString(T)

    def parseString(self, inputStr):
        resultStr = ""

        for ch in inputStr:
            if ch == '#':
                if len(resultStr) > 0:
                    resultStr = resultStr[:-1]
            else:
                resultStr += ch

        return resultStr

obj = Solution()
print(obj.backspaceCompare("y#fo##f", "y#f#o#f"))
