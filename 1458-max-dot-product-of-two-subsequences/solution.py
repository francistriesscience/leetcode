class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        prev = [float("-inf")] * (m + 1)
        for i in range(1, n + 1):
            dp = [float("-inf")] * (m + 1)
            for j in range(1, m + 1):
                product = nums1[i-1] * nums2[j-1]
                term1 = product + max(0, prev[j-1])
                term2 = prev[j]
                term3 = dp[j-1]
                dp[j] = max(term1, term2, term3)
            prev = dp
        return int(prev[m])