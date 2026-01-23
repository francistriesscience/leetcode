class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
            
        vals = list(nums)
        
        L = [-1] * n
        R = [-1] * n
        for i in range(n):
            if i > 0: L[i] = i - 1
            if i < n - 1: R[i] = i + 1
            
        unsorted_indices = set()
        for i in range(n - 1):
            if vals[i] > vals[i+1]:
                unsorted_indices.add(i)
                
        if not unsorted_indices:
            return 0
            
        pq = []
        for i in range(n - 1):
            heapq.heappush(pq, (vals[i] + vals[i+1], i))
            
        alive = [True] * n
        ops = 0
        
        while unsorted_indices:
            while True:
                curr_sum, u = heapq.heappop(pq)
                
                if not alive[u]:
                    continue
                    
                v = R[u]
                
                if v != -1 and vals[u] + vals[v] == curr_sum:
                    break
            
            new_val = curr_sum
            vals[u] = new_val
            alive[v] = False
            
            w = R[v] 
            R[u] = w
            if w != -1:
                L[w] = u
            
            unsorted_indices.discard(u)
            unsorted_indices.discard(v) 
            left_neighbor = L[u]
            if left_neighbor != -1:
                unsorted_indices.discard(left_neighbor)
                
            if left_neighbor != -1:
                if vals[left_neighbor] > vals[u]:
                    unsorted_indices.add(left_neighbor)
                    
            if w != -1:
                if vals[u] > vals[w]:
                    unsorted_indices.add(u)
                    
            if w != -1:
                heapq.heappush(pq, (vals[u] + vals[w], u))
            if left_neighbor != -1:
                heapq.heappush(pq, (vals[left_neighbor] + vals[u], left_neighbor))
                
            ops += 1
            
        return ops
