from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_abs_sum = 0
        min_abs_val = float('inf')
        negative_count = 0
        
        for row in matrix:
            for val in row:
                abs_val = abs(val)
                total_abs_sum += abs_val
                
                if val < 0:
                    negative_count += 1
                
                if abs_val < min_abs_val:
                    min_abs_val = abs_val
        
        if negative_count % 2 == 0:
            return total_abs_sum
        
        return total_abs_sum - (2 * min_abs_val)
