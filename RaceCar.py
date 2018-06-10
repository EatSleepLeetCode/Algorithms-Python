class Solution(object):
    def racecar(self, target):
        queue = []
        visited = set()

        queue.append(Node(0, 1))
        visited.add("01")
        depth = -1

        while queue:
            depth += 1
            size = len(queue)

            for i in xrange(size):
                curr = queue.pop(0)

                if curr.pos == target:
                    return depth

                nei = Node(curr.pos + curr.speed, curr.speed << 1)  # accelerate instruction
                neiKey = str(nei.pos) + str(nei.speed)

                if neiKey not in visited and 0 < nei.pos and nei.pos < (target << 1):
                    queue.append(nei)
                    visited.add(neiKey)

                nei = Node(curr.pos, -1 if curr.speed > 0 else 1)  # reverse instruction
                neiKey = str(nei.pos) + str(nei.speed)

                if neiKey not in visited and 0 < nei.pos and nei.pos < (target << 1):
                    queue.append(nei)
                    visited.add(neiKey)

        return -1


class Node(object):
    pos, speed = 0, 0

    def __init__(self, pos, speed):
        self.pos = pos
        self.speed = speed
