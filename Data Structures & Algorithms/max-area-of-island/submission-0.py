class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_ = 0
        def dfs (r,c):
            if r <0 or c< 0 or r == rows or c == cols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            
            number = 1 + dfs(r+1,c) + dfs(r,c+1) + dfs(r-1,c) + dfs(r,c-1)
            return number

        for r in range(rows):
            for c in range(cols):
                max_ = max(dfs(r,c),max_)

        return max_