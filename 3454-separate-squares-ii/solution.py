class SegmentTree:
    def __init__(self, x_coords):
        self.x_coords = x_coords
        self.n = len(x_coords) - 1
        self.count = [0] * (4 * self.n)
        self.length = [0.0] * (4 * self.n)

    def update(self, node, start, end, l, r, val):
        if r <= self.x_coords[start] or l >= self.x_coords[end]:
            return
        
        if l <= self.x_coords[start] and self.x_coords[end] <= r:
            self.count[node] += val
        else:
            mid = (start + end) // 2
            self.update(2 * node, start, mid, l, r, val)
            self.update(2 * node + 1, mid, end, l, r, val)
        
        if self.count[node] > 0:
            self.length[node] = self.x_coords[end] - self.x_coords[start]
        else:
            if start + 1 == end:
                self.length[node] = 0.0
            else:
                self.length[node] = self.length[2 * node] + self.length[2 * node + 1]

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        x_set = set()
        for x, y, l in squares:
            x_set.add(x)
            x_set.add(x + l)
        
        sorted_x = sorted(list(x_set))
        
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            
        events.sort(key=lambda x: x[0])

        st = SegmentTree(sorted_x)
        total_area = 0.0
        prev_y = events[0][0]
        
        for y, type, x1, x2 in events:
            width = st.length[1] 
            total_area += width * (y - prev_y)
            st.update(1, 0, len(sorted_x) - 1, x1, x2, type)
            prev_y = y
            
        target = total_area / 2.0
        
        st = SegmentTree(sorted_x)
        current_area = 0.0
        prev_y = events[0][0]
        
        for y, type, x1, x2 in events:
            current_width = st.length[1]
            height = y - prev_y
            segment_area = current_width * height
            
            if current_area + segment_area >= target:
                if current_width == 0:
                    return prev_y
                return prev_y + (target - current_area) / current_width
            
            current_area += segment_area
            st.update(1, 0, len(sorted_x) - 1, x1, x2, type)
            prev_y = y
            
        return float(prev_y)
