class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = float('inf')
        dist = [[INF] * 26 for _ in range(26)]
        
        for i in range(26):
            dist[i][i] = 0
            
        for src, dst, c in zip(original, changed, cost):
            u = ord(src) - ord('a')
            v = ord(dst) - ord('a')
            dist[u][v] = min(dist[u][v], c)
            
        for k in range(26):
            for i in range(26):
                if dist[i][k] == INF: 
                    continue
                for j in range(26):
                    if dist[k][j] == INF:
                        continue
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
        total_cost = 0
        for s_char, t_char in zip(source, target):
            if s_char == t_char:
                continue
                
            u = ord(s_char) - ord('a')
            v = ord(t_char) - ord('a')
            
            if dist[u][v] == INF:
                return -1
            
            total_cost += dist[u][v]
            
        return total_cost
