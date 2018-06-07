import sys

class Solution:


    def shortestPathLength(self, graph):
        n = len(graph)
        visited = [[False for x in range(n)] for y in range(1 << n)]
        cache = [[-1 for x in range(n)] for y in range(1 << n)]
        minDist = sys.maxsize
        for i in range(n):
            minDist = min(minDist, self.dfs(graph, visited, cache, i, n, 1 << i))

        return minDist

    def dfs(self, graph, visited, cache, src, n, status):
        if status == (1 << n) - 1:
            return 0

        if cache[status][src] != -1:
            return cache[status][src]

        shortest = sys.maxsize

        for nei in graph[src]:
            updStatus = status | (1 << nei)

            if not visited[updStatus][nei]:
                visited[updStatus][nei] = True
                minDist = self.dfs(graph, visited, cache, nei, n, updStatus)

                if minDist != -1:
                    shortest = min(shortest, minDist + 1)

                visited[updStatus][nei] = False

        if shortest == sys.maxsize:
            return -1

        cache[status][src] = shortest
        return cache[status][src]

obj = Solution()
print(obj.shortestPathLength([[1,2,3],[0],[0],[0]]))