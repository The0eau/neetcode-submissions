class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges :
            if n == 1:
                return True
            else:
                return False

        adj = defaultdict(list)
        in_degree = [0] * n
        
        for i, j  in edges:
            adj[i].append(j)
            adj[j].append(i)            

        # File contenant les cours sans aucun prérequis initial
        queue = deque([0])

        completed = 0
        in_degree[0] = 1
        # Traitement par niveau (Tri Topologique)
        while queue:
            current = queue.popleft()
            completed += 1
            
            for neighbor in adj[current]:
                if in_degree[neighbor] >0 :
                    return False
                in_degree[neighbor] = 1 + in_degree[current]
                adj[neighbor].remove(current)
                queue.append(neighbor)
                    
        return completed == n