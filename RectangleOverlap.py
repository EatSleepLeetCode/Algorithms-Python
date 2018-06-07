class Solution:
    def isRectangleOverlap1(self, rec1, rec2):
        bottom1, left1, top1, right1 = rec1[0], rec1[1], rec1[2], rec1[3]
        bottom2, left2, top2, right2 = rec2[0], rec2[1], rec2[2], rec2[3]

        if left1 >= right2 or left2 >= right1:
            return False

        if bottom1 >= top2 or bottom2 >= top1:
            return False

        return True

    def isRectangleOverlap(self, rec1, rec2):
        bottom1, left1, top1, right1 = rec1[0], rec1[1], rec1[2], rec1[3]
        bottom2, left2, top2, right2 = rec2[0], rec2[1], rec2[2], rec2[3]

        if max(left1, left2) < min(right1, right2) and \
                max(bottom1, bottom2) < min(top1, top2):
            return True

        return False