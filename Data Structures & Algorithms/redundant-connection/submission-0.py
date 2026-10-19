class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # n sommets numérotés de 1 à n
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(node: int) -> int:
            # Compression de chemin
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1: int, node2: int) -> bool:
            root1, root2 = find(node1), find(node2)
            
            if root1 == root2:
                return False
            
            # Union par rang
            if rank[root1] > rank[root2]:
                parent[root2] = root1
                rank[root1] += rank[root2]
            else:
                parent[root1] = root2
                rank[root2] += rank[root1]
            return True

        for u, v in edges:
            # Si l'union échoue, c'est l'arête redondante
            if not union(u, v):
                return [u, v]

        return []

            
                