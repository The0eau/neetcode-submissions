class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ligne = [1]*n
        for _ in range(1,m):
            for j in range(1,n):
                ligne[j] += ligne[j-1]
        return ligne[-1]