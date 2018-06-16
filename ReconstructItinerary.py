import collections

class Solution:
    def findItinerary(self, tickets):
        adj = collections.defaultdict(list)

        for a, b in sorted(tickets)[::-1]:  # sorted(tickets, reverse = True) will also work
            adj[a] += b,

        result = []

        def dfs(departure):
            while adj[departure]:
                dfs(adj[departure].pop())

            result.append(departure)

        dfs("JFK")
        return result[::-1]  # Reverse result list


obj = Solution()
print(obj.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))