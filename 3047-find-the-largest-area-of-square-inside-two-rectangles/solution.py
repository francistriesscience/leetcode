class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_side = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                min_x = max(bottomLeft[i][0], bottomLeft[j][0])
                max_x = min(topRight[i][0], topRight[j][0])
                
                min_y = max(bottomLeft[i][1], bottomLeft[j][1])
                max_y = min(topRight[i][1], topRight[j][1])
                
                if min_x < max_x and min_y < max_y:
                    width = max_x - min_x
                    height = max_y - min_y
                    
                    side = min(width, height)
                    
                    if side > max_side:
                        max_side = side
                        
        return max_side * max_side
