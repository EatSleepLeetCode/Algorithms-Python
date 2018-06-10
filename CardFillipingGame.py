class Solution(object):
    def flipgame1(self, fronts, backs):
        sameValsSet = []
        n, result = len(fronts), sys.maxsize

        for i in xrange(n):
            if fronts[i] == backs[i]:
                sameValsSet.append(fronts[i])

        for i in xrange(n):
            if fronts[i] not in sameValsSet:
                result = min(result, fronts[i])
            if backs[i] not in sameValsSet:
                result = min(result, backs[i])

        return 0 if result == sys.maxsize else result

    def flipgame(self, fronts, backs):
        sameValsSet = []
        n, result = len(fronts), sys.maxsize

        # Very Fast operation
        sameValsSet = {val for index, val in enumerate(fronts) if val == backs[index]}

        for val in itertools.chain(fronts, backs):
            if val not in sameValsSet:
                result = min(result, val)

        return 0 if result == sys.maxsize else result