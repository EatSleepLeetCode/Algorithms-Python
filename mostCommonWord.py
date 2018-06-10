class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        bannedSet = set(banned)
        freqMap = collections.Counter(word.strip("!?',;.") for word in paragraph.lower().split())

        maxFreq, result = 0, ""

        for word in freqMap:
            if word not in bannedSet and freqMap[word] > maxFreq:
                maxFreq, result = freqMap[word], word

        return result
    