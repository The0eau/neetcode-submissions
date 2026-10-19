class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_list = []
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            adj[prereq].append(course)  # prereq -> course
            in_degree[course] += 1
            
        # File contenant les cours sans aucun prérequis initial
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed = 0
        
        # Traitement par niveau (Tri Topologique)
        while queue:
            current = queue.popleft()
            completed += 1
            if current not in course_list:
                course_list.append(current)
            for neighbor in adj[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        if completed != numCourses:
            return []
        else : 
            return course_list