class Solution(object):
    def bestRotation(self, A):
        best, curr, result, n = -sys.maxsize - 1, 0, -1, len(A)
        bad = [0] * n

        for i in xrange(n):
            left = (i - A[i] + 1 + n) % n
            right = (i + 1) % n

            bad[left] += -1
            bad[right] += 1

            if left > right:
                bad[0] += -1

        for i in xrange(n):
            curr += bad[i]
            if best < curr:
                best = curr
                result = i

        return result
