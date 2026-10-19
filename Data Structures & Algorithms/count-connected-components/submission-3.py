class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:        
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        counter = 0
        
        # On parcourt directement tous les nœuds de 0 à n-1
        for i in range(n):
            if i not in visited:
                counter += 1
                visited.add(i)
                queue = deque([i])
                
                while queue:
                    node = queue.popleft()
                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                            
        return counter