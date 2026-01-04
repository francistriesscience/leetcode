import math
from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0
        cache = {}

        for num in nums:
            if num in cache:
                total_sum += cache[num]
                continue
            
            if num < 6:
                cache[num] = 0
                continue

            div_sum = 0
            count = 0
            limit = int(math.isqrt(num))
            
            for d in range(1, limit + 1):
                if num % d == 0:
                    if d * d == num:
                        count += 1
                        div_sum += d
                    else:
                        count += 2
                        div_sum += d + (num // d)
                    
                    if count > 4:
                        break
            
            if count == 4:
                cache[num] = div_sum
                total_sum += div_sum
            else:
                cache[num] = 0
                
        return total_sum
