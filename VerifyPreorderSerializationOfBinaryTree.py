class Solution:
    def isValidSerialization(self, preorder):
        arr = preorder.split(",")
        degree = -1

        for val in arr:
            degree += 1

            if degree > 0:
                return False

            if val is not "#":
                degree -= 2

        return degree == 0