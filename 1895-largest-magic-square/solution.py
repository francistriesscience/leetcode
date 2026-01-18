class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        row_prefix = [[0] * (n + 1) for _ in range(m)]
        col_prefix = [[0] * n for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                row_prefix[i][j+1] = row_prefix[i][j] + grid[i][j]
                
        for j in range(n):
            for i in range(m):
                col_prefix[i+1][j] = col_prefix[i][j] + grid[i][j]
                
        def get_row_sum(r, c1, c2):
            return row_prefix[r][c2+1] - row_prefix[r][c1]
            
        def get_col_sum(c, r1, r2):
            return col_prefix[r2+1][c] - col_prefix[r1][c]
            
        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    d1_sum = 0
                    d2_sum = 0
                    for i in range(k):
                        d1_sum += grid[r+i][c+i]
                        d2_sum += grid[r+i][c+k-1-i]
                        
                    if d1_sum != d2_sum:
                        continue
                        
                    target = d1_sum
                    
                    is_magic = True
                    for i in range(k):
                        if get_row_sum(r+i, c, c+k-1) != target:
                            is_magic = False
                            break
                        if get_col_sum(c+i, r, r+k-1) != target:
                            is_magic = False
                            break
                    
                    if is_magic:
                        return k
                        
        return 1
