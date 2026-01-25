class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        max_pair_sum = 0
        n = len(nums)
        
        for i in range(n // 2):
            current_sum = nums[i] + nums[n - 1 - i]
            if current_sum > max_pair_sum:
                max_pair_sum = current_sum
                
        return max_pair_sum
