class Solution:
    def shiftingLetters(self, S, shifts):
        n = len(shifts)
        # result = ""
        result = []

        for i in range(n):
            shifts[i] = shifts[i] % 26

        for i in range(n - 2, -1, -1):
            shifts[i] += shifts[i + 1]

        for i in range(n):
            # result += (self.shift(S[i], shifts[i] % 26))
            result.append(self.shift(S[i], shifts[i] % 26))

        # return result
        return "".join(result)

    def shift(self, ch, shift):
        while shift > 0:
            if ch == 'z':
                ch = 'a'
            else:
                ch = chr(ord(ch) + 1)

            shift -= 1
        return ch