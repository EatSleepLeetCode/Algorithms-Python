class Solution:
    def combinationSum3(self, k, n):
        curr = []
        result = []
        self.helper(k, n, 0, 1, curr, result)
        return result

    def helper(self, k, n, currSum, index, curr, result):
        if len(curr) == k:
            if currSum == n:
                result.append(list(curr))
            return

        for i in range(index, 10):
            if currSum + i > n:
                continue

            if i in curr:
                continue

            curr.append(i)
            self.helper(k, n, currSum + i, i + 1, curr, result)
            curr.remove(curr[-1])  # curr.pop() also works