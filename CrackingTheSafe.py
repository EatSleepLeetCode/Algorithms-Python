class Solution:
    sb = ""  # Strings are immutable

    def crackSafe(self, n, k):
        visited = []
        target = k ** n

        for i in range(n):
            self.sb = self.sb + "0"

        visited.append(self.sb)
        self.dfs(n, k, target, visited)
        return self.sb

    def dfs(self, n, k, target, visited):
        if len(visited) == target:
            return True

        prev = self.sb[len(self.sb) - n + 1: ]

        for i in range(k):
            nei = prev + str(i)

            if nei in visited:
                continue

            self.sb = self.sb + str(i)
            visited.append(nei)

            if self.dfs(n, k, target, visited):
                return True
            else:
                visited.remove(nei)
                self.sb = self.sb[:-1]

        return False

obj = Solution()
print(obj.crackSafe(1, 2))