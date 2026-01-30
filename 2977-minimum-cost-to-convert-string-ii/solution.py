class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        if len(target) != n:
            return -1
            
        unique_strs = set(original) | set(changed)
        str_to_id = {s: i for i, s in enumerate(unique_strs)}
        id_to_str = {i: s for s, i in str_to_id.items()}
        num_nodes = len(unique_strs)
        
        adj = [[] for _ in range(num_nodes)]
        for u_str, v_str, c in zip(original, changed, cost):
            u = str_to_id[u_str]
            v = str_to_id[v_str]
            adj[u].append((v, c))
            
        inf = float('inf')
        min_costs = [[inf] * num_nodes for _ in range(num_nodes)]
        
        for start_node in range(num_nodes):
            min_costs[start_node][start_node] = 0
            pq = [(0, start_node)]
            
            while pq:
                d, u = heapq.heappop(pq)
                
                if d > min_costs[start_node][u]:
                    continue
                
                for v, c in adj[u]:
                    if min_costs[start_node][u] + c < min_costs[start_node][v]:
                        min_costs[start_node][v] = min_costs[start_node][u] + c
                        heapq.heappush(pq, (min_costs[start_node][v], v))
                        
        dp = [inf] * (n + 1)
        dp[n] = 0
        
        possible_lengths = set(len(s) for s in original)
        
        for i in range(n - 1, -1, -1):
            if source[i] == target[i]:
                dp[i] = min(dp[i], dp[i+1])
            
            for length in possible_lengths:
                j = i + length
                if j > n:
                    continue
                
                sub_s = source[i:j]
                sub_t = target[i:j]
                
                if sub_s in str_to_id and sub_t in str_to_id:
                    u = str_to_id[sub_s]
                    v = str_to_id[sub_t]
                    if min_costs[u][v] < inf:
                         if dp[j] < inf:
                            dp[i] = min(dp[i], min_costs[u][v] + dp[j])
                            
        return dp[0] if dp[0] < inf else -1

