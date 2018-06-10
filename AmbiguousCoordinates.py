import itertools

class Solution(object):
    def ambiguousCoordinates(self, S):
        def make(frag):
            n = len(frag)
            for d in xrange(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                if ((not left.startswith("0") or left == "0")
                        and (not right.endswith("0"))):
                    yield left + ("." if d != n else "") + right

        S = S[1:-1]
        return ["({}, {})".format(*cand)
                for i in xrange(1, len(S))
                for cand in itertools.product(make(S[:i]), make(S[i:]))]