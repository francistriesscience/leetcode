class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(l * l for _, _, l in squares)
        target = total_area / 2.0
        
        events = {}
        for _, y, l in squares:
            events[y] = events.get(y, 0) + l
            events[y + l] = events.get(y + l, 0) - l
            
        sorted_y = sorted(events.keys())
        
        current_width = 0
        current_area = 0.0
        
        for i in range(len(sorted_y) - 1):
            y1 = sorted_y[i]
            y2 = sorted_y[i+1]
            
            current_width += events[y1]
            
            height = y2 - y1
            segment_area = current_width * height
            
            if current_area + segment_area >= target:
                if current_width == 0:
                    return y1
                return y1 + (target - current_area) / current_width
            
            current_area += segment_area
            
        return float(sorted_y[-1])
