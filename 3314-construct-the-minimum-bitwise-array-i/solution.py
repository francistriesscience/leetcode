class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for val in nums:
            if val == 2:
                ans.append(-1)
            else:
                trailing_ones = 0
                temp = val
                while temp & 1:
                    trailing_ones += 1
                    temp >>= 1
                
                res = val & ~(1 << (trailing_ones - 1))
                ans.append(res)
                
        return ans
