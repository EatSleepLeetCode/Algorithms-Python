class Solution:
    def pushDominoes(self, dominoes):
        force, n = 0, len(dominoes)
        forces = [0 for _ in range(n)]

        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] += force

        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] -= force

        result = "".join("R" if forces[i] > 0 else "L" if forces[i] < 0 else "." for i in range(n))

        return result

obj = Solution()
print(obj.pushDominoes(".L.R...LR..L.."))