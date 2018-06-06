def patternFound(input, pattern):
    prefixArr = [0 for _ in range(len(pattern))]
    buildPrefixArray(prefixArr, pattern)
    i,j = 0, 0
    while i < len(input) and j < len(pattern):
        if input[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j > 0:
                j = prefixArr[j - 1]
            elif j == 0:
                i += 1

    if j == len(pattern):
        return True

    return False


def buildPrefixArray(arr, pattern):
    i, j, n = 1, 0, len(pattern)

    while i < n:
        if pattern[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j > 0:
                j = arr[j - 1]
            elif j == 0:
                j = 0
                arr[i] = 0
                i += 1

print(patternFound("abcdefasbcagsa", "asbg"))
print(patternFound("acacabacacabacacaXacacabacacabacacac", "acacabacacabacacac"))