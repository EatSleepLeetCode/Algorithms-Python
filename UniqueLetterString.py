def uniqueLetterString(self, S):
    result = 0
    posMap = collections.defaultdict(list)
    for i, ch in enumerate(S):
        posMap[ch].append(i)

    for vals in posMap.values():
        vals = [-1] + vals + [len(S)]
        for i in xrange(1, len(vals) - 1):
            result += (vals[i] - vals[i - 1]) * (vals[i + 1] - vals[i])

    return result % 10 ** 7