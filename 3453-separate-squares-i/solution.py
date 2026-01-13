class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        min_y = float('inf')
        max_y = float('-inf')

        for _, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)

        target = total_area / 2.0
        
        low = min_y
        high = max_y
        
        for _ in range(100):
            mid = (low + high) / 2
            current_area = 0
            for _, y, l in squares:
                if y >= mid:
                    continue
                elif y + l <= mid:
                    current_area += l * l
                else:
                    current_area += l * (mid - y)

            if current_area >= target:
                high = mid
            else:
                low = mid
                
        return high
