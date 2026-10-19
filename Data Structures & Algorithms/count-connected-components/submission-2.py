class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:        
        
       
        adj = defaultdict(list)
        set_ = set()
        for u, v in edges:
            set_.add(u)
            set_.add(v)
            adj[u].append(v)
            adj[v].append(u)
        
        # BFS à partir du nœud 0
        visited = set()
        counter = 0
        for i in set_ :
            if i not in visited:
                queue = deque([i])
                visited.add(i)
                while queue:
                    node = queue.popleft()
                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                counter +=1

        return counter + n - len(set_)