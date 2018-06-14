class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        left = self.leftDepth(root)
        right = self.rightDepth(root)

        if left == right:
            return (1 << left) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def leftDepth(self, root):
        left = 0

        while root is not None:
            root = root.left
            left += 1

        return left

    def rightDepth(self, root):
        right = 0

        while root is not None:
            root = root.right
            right += 1

        return right