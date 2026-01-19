class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = P[i-1][j] + P[i][j-1] - P[i-1][j-1] + mat[i-1][j-1]
                
        def get_rect_sum(r1, c1, r2, c2):
            return P[r2][c2] - P[r1][c2] - P[r2][c1] + P[r1][c1]
            
        max_side = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                k = max_side + 1
                if i >= k and j >= k:
                    total = get_rect_sum(i-k, j-k, i, j)
                    if total <= threshold:
                        max_side += 1
                        
        return max_side
