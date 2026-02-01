class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))
            
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        
        pq = [(0, 0)]
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if d > min_dist[u]:
                continue
            
            if u == n - 1:
                return d
            
            for v, w in adj[u]:
                new_cost = d + w
                if new_cost < min_dist[v]:
                    min_dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))
                    
        return -1 if min_dist[n-1] == float('inf') else min_dist[n-1]
