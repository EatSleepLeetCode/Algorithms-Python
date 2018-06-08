class Solution(object):
    def largestIsland(self, grid):
        ds = DisjointSet()
        rows, cols, neiRow, neiCol = len(grid), len(grid[0]), -1, -1
        neiParent, parent, combined, result = -1, -1, 0, 1
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        parentSet = []

        for i in xrange(rows):
            for j in xrange(cols):
                if grid[i][j] == 1:
                    ds.makeSet(i * cols + j)

        for i in xrange(rows):
            for j in xrange(cols):
                if grid[i][j] is not 1:
                    continue

                for dirArr in dirs:
                    neiRow = i + dirArr[0]
                    neiCol = j + dirArr[1]

                    if neiRow < 0 or neiRow >= rows or neiCol < 0 or \
                            neiCol >= cols or grid[neiRow][neiCol] == 0:
                        continue

                    ds.unionSet(i * cols + j, neiRow * cols + neiCol)
                    parent = ds.findSet(i * cols + j)
                    result = max(result, ds.getArea(parent))

        for i in xrange(rows):
            for j in xrange(cols):
                if grid[i][j] is not 0:
                    continue
                parentSet = []
                combined = 1

                for dirArr in dirs:
                    neiRow = i + dirArr[0]
                    neiCol = j + dirArr[1]

                    if neiRow < 0 or neiRow >= rows or neiCol < 0 or \
                            neiCol >= cols or grid[neiRow][neiCol] == 0:
                        continue

                    neiParent = ds.findSet(neiRow * cols + neiCol)

                    if neiParent in parentSet:
                        continue

                    combined += ds.getArea(neiParent)
                    parentSet.append(neiParent)

                result = max(result, combined)

        return result


class Node:
    val = 0
    parent = None
    rank = 0
    area = 0


class DisjointSet:
    nodeMap = {}

    def makeSet(self, val):
        node = Node()
        node.val = val
        node.parent = node
        node.rank = 0
        node.area = 1
        self.nodeMap[val] = node

    def unionSet(self, val1, val2):
        node1 = self.nodeMap[val1]
        node2 = self.nodeMap[val2]

        parent1 = self.findSetNode(node1)
        parent2 = self.findSetNode(node2)

        if parent1 == parent2:
            return

        if parent1.rank >= parent2.rank:
            parent2.parent = parent1
            parent1.area += parent2.area

            if parent1.rank == parent2.rank:
                parent1.rank += 1
        else:
            parent1.parent = parent2
            parent2.area += parent1.area

    def findSet(self, nodeVal):
        node = self.nodeMap[nodeVal]
        return self.findSetNode(node).val

    def findSetNode(self, node):
        while node != node.parent:
            node.parent = node.parent.parent
            node = node.parent
        return node

    def getArea(self, nodeVal):
        return self.nodeMap[nodeVal].area
