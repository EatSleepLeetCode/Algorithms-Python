class Solution(object):
    def makesquare(self, nums):
        n = len(nums)
        sides = [0] * 4

        if n < 4:
            return False

        numsSum = sum(nums)

        if numsSum % 4 != 0:
            return False

        target = numsSum / 4

        nums.sort(reverse=True)

        if any(num > target for num in nums):
            return False

        return self.dfs(nums, sides, target, 0)

    def dfs(self, nums, sides, target, index):
        if index == len(nums):
            return all(side == target for side in sides)

            # Below could be written as above:

            # if sides[0] == target and sides[1] == target and sides[2] == target:
            #     return True
            # else:
            #     return False

        for i in range(4):
            if sides[i] + nums[index] > target:
                continue

            sides[i] += nums[index]

            if self.dfs(nums, sides, target, index + 1):
                return True

            sides[i] -= nums[index]

        return False

