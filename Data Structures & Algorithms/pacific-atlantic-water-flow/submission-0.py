class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()

        def dfs(r, c, visited):
            visited.add((r, c))
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visited)

        
        for r in range(rows):
            dfs(r, 0, pacific_visited)       
            dfs(r, cols - 1, atlantic_visited) 

        for c in range(cols):
            dfs(0, c, pacific_visited)       
            dfs(rows - 1, c, atlantic_visited) 

       
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_visited and (r, c) in atlantic_visited:
                    result.append([r, c])

        return result