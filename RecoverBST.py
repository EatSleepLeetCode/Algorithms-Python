import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def recoverTree(self, root):
        self.first = None  # use self to reference and use it in traverseInOrder
        self.second = None
        self.prev = TreeNode(-sys.maxsize - 1)  # setting to minimum integer value

        self.traverseInOrder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def traverseInOrder(self, root):
        stack = []

        while root != None or len(stack) > 0:
            if root != None:
                stack.append(root)
                root = root.left
            else:
                curr = stack.pop()

                if self.first == None and self.prev.val >= curr.val:
                    self.first = self.prev
                if self.first != None and self.prev.val >= curr.val:
                    self.second = curr

                self.prev = curr
                root = curr.right