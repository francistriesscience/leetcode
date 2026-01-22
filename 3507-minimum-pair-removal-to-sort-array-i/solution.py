class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0
        
        while True:
            is_sorted = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    is_sorted = False
                    break
            
            if is_sorted:
                return ops
            
            min_sum = float('inf')
            idx = -1
            
            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i+1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    idx = i
            
            new_val = nums[idx] + nums[idx+1]
            nums[idx] = new_val
            nums.pop(idx + 1)
            
            ops += 1
