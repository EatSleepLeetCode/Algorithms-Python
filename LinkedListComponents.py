# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def numComponents(self, head, G):
        count, curr = 0, head
        gSet = set(G)

        while curr:
            if curr.val in gSet and (curr.next == None or curr.next.val not in gSet):
                count += 1
            curr = curr.next

        return count