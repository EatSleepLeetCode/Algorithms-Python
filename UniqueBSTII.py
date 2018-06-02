# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def generateTrees(self, n):
        result = [[] for _ in range(n + 1)]

        if n == 0:
            return result[0]

        result[0].append(None)

        for length in range(1, n + 1):
            for j in range(length):
                for nodeL in result[j]:
                    for nodeR in result[length - j - 1]:
                        node = TreeNode(j + 1)
                        node.left = nodeL
                        node.right = self.clone(nodeR, j + 1)
                        result[length].append(node)
        return result[n]

    def clone(self, root, offset):
        if root == None:
            return None

        f = self.clone

        node = TreeNode(root.val + offset)
        node.left = f(root.left, offset)
        node.right = f(root.right, offset)
        return node