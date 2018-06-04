import collections

class Solution:

    def isNStraightHand(self, hand, W):
        cardMap = collections.Counter(hand)
        for card in sorted(cardMap):
            freq = cardMap[card]
            if freq <= 0:
                continue
            for i in range(W - 1, 0, -1):
                if cardMap[card + i] < freq:
                    return False
                cardMap[card + i] = cardMap[card + i] - freq
        return True

obj = Solution()
print(obj.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
print(obj.isNStraightHand([1,2,3,4,5,6], 2))