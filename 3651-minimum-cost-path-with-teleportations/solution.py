class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:

        m, n = len(grid), len(grid[0])
        
        unique_vals = sorted(list(set(val for row in grid for val in row)))
        val_to_idx = {val: i for i, val in enumerate(unique_vals)}
        num_vals = len(unique_vals)
        
        cells_by_val_idx = [[] for _ in range(num_vals)]
        for r in range(m):
            for c in range(n):
                idx = val_to_idx[grid[r][c]]
                cells_by_val_idx[idx].append((r, c))
        
        cell_block_size = m * n
        total_cells = cell_block_size * (k + 1)
        
        hub_block_size = num_vals
        total_hubs = hub_block_size * k
        
        total_nodes = total_cells + total_hubs
        
        def get_cell_id(r, c, k_state):
            return (k_state * cell_block_size) + (r * n + c)
            
        def get_hub_id(v_idx, k_state):
            return total_cells + (k_state * hub_block_size) + v_idx
            
        dist = [float('inf')] * total_nodes
        start_id = get_cell_id(0, 0, 0)
        dist[start_id] = 0
        
        pq = [(0, start_id)]
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if d > dist[u]:
                continue
            
            if u < total_cells:
                rem = u
                c_idx = rem % n; rem //= n
                r_idx = rem % m; rem //= m
                k_state = rem
                
                if r_idx == m - 1 and c_idx == n - 1:
                    return d
                
                for dr, dc in [(0, 1), (1, 0)]:
                    nr, nc = r_idx + dr, c_idx + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        new_cost = d + grid[nr][nc]
                        nid = get_cell_id(nr, nc, k_state)
                        if new_cost < dist[nid]:
                            dist[nid] = new_cost
                            heapq.heappush(pq, (new_cost, nid))
                            
                if k_state < k:
                    v_idx = val_to_idx[grid[r_idx][c_idx]]
                    hid = get_hub_id(v_idx, k_state)
                    if d < dist[hid]:
                        dist[hid] = d
                        heapq.heappush(pq, (d, hid))
                        
            else:
                rem = u - total_cells
                v_idx = rem % hub_block_size
                k_state = rem // hub_block_size
                
                if v_idx > 0:
                    lower_hid = get_hub_id(v_idx - 1, k_state)
                    if d < dist[lower_hid]:
                        dist[lower_hid] = d
                        heapq.heappush(pq, (d, lower_hid))
                        
                next_k = k_state + 1
                for lr, lc in cells_by_val_idx[v_idx]:
                    target_cell_id = get_cell_id(lr, lc, next_k)
                    if d < dist[target_cell_id]:
                        dist[target_cell_id] = d
                        heapq.heappush(pq, (d, target_cell_id))
                        
        return -1
