def largeGroupPositions(self, S):
    i, startIndex, count, n = 0, 0, 0, len(S)
    result = []

    while i < n:
        startIndex = i
        count = 0
        ch = S[i]

        while i < n and ch == S[i]:
            count += 1
            i += 1

        if count >= 3:
            result.append([startIndex, startIndex + count - 1])

    return result