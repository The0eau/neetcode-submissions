class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graphe = collections.defaultdict(list)
        for u, v , w in times:
            graphe[u].append((v,w))

        min_heap = [(0,k)]


        temps_min = {}

        while min_heap : 
            temps, u = heapq.heappop(min_heap)

            if u in temps_min :
                continue
            temps_min[u] = temps

            for v, poids in graphe[u]:
                if v not in temps_min : 
                    heapq.heappush(min_heap, (temps+poids,v))

        if len(temps_min) == n:
            return max(temps_min.values())
        return -1