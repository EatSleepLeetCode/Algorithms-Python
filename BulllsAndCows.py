class Solution:
    def getHint(self, secret, guess):
        bulls, cows, n = 0, 0, len(secret)
        nums = [0] * 10

        for i in range(n):
            s = ord(secret[i]) - ord('0')
            g = ord(guess[i]) - ord('0')

            if s == g:
                bulls += 1
            else:
                if nums[s] < 0:
                    cows += 1
                nums[s] += 1

                if nums[g] > 0:
                    cows += 1
                nums[g] -= 1

        return str(bulls) + "A" + str(cows) + "B"