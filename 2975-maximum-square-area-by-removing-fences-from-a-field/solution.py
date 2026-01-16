class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        h_lines = sorted(hFences + [1, m])
        v_lines = sorted(vFences + [1, n])
        
        h_gaps = set()
        for i in range(len(h_lines)):
            for j in range(i + 1, len(h_lines)):
                h_gaps.add(h_lines[j] - h_lines[i])
                
        max_side = -1
        
        for i in range(len(v_lines)):
            for j in range(i + 1, len(v_lines)):
                gap = v_lines[j] - v_lines[i]
                if gap in h_gaps:
                    if gap > max_side:
                        max_side = gap
                        
        if max_side == -1:
            return -1
            
        return (max_side * max_side) % MOD
