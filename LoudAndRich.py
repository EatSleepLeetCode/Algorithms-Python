class Solution:
    def loudAndRich(self, richer, quiet):
        n, adj = len(quiet), {}
        answer = [-1] * n

        for i in range(n):
            adj[i] = []

        for i in range(len(richer)):
            adj[richer[i][1]].append(richer[i][0])

        for i in range(n):
            self.dfs(adj, i, quiet, answer)

        return answer

    def dfs(self, adj, src, quiet, answer):
        if answer[src] >= 0:
            return answer[src]

        answer[src] = src

        adjList = adj[src]

        if adjList is not None:
            for person in adjList:
                candidate = self.dfs(adj, person, quiet, answer)

                if quiet[answer[src]] > quiet[candidate]:
                    answer[src] = candidate

        return answer[src]