class Solution:
    def numSimilarGroups(self, A):
        ds = DisjointSet()

        for strVal in A:
            ds.makeSet(strVal)

        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                if self.isSimilar(A[i], A[j]):
                    ds.unionSet(A[i], A[j])
        return ds.size

    def isSimilar(self, str1, str2):
        i, count = 0, 0
        while i < len(str1):
            if str1[i] != str2[i]:
                count += 1
            i += 1
        if count == 2:
            return True

        return False


class Node:
    val = ""
    parent = None
    rank = 0


class DisjointSet:
    nodeMap = {}
    size = 0

    def makeSet(self, val):

        if val in self.nodeMap:
            return

        node = Node()
        node.val = val
        node.parent = node
        node.rank = 0
        self.nodeMap[val] = node
        self.size += 1

    def unionSet(self, str1, str2):
        node1 = self.nodeMap[str1]
        node2 = self.nodeMap[str2]

        parent1 = self.findSetNode(node1)
        parent2 = self.findSetNode(node2)

        if parent1 == parent2:
            return

        self.size -= 1

        if parent1.rank >= parent2.rank:
            parent2.parent = parent1

            if parent1.rank == parent2.rank:
                parent1.rank += 1
        else:
            parent1.parent = parent2

    def findSet(self, strVal):
        node = self.nodeMap[strVal]
        return self.findSetNode(node).val

    def findSetNode(self, node):
        while node != node.parent:
            node.parent = node.parent.parent
            node = node.parent
        return node

obj = Solution()
print(obj.numSimilarGroups(["tars","rats","arts","star"]))