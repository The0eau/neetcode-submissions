class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return 
        
        rows, cols = len(board), len(board[0])
        queue = deque()
        bann = set()
        
        # Add only boundary cells that contain "O"
        for r in range(rows):
            for c in range(cols):
                # Check if the cell is on any of the 4 borders
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    if board[r][c] == "O":
                        queue.append((r, c))
                        bann.add((r, c))
                        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS to mark all boundary-connected "O"s
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O" and (nr, nc) not in bann:
                    queue.append((nr, nc))
                    bann.add((nr, nc))
                    
        # Flip any "O" not connected to the boundary to "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in bann:
                    board[r][c] = "X"
                        