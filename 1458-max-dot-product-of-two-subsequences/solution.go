func maxDotProduct(nums1 []int, nums2 []int) int {
	m := len(nums2)
	prev := make([]int, m+1)

	const minVal = math.MinInt32

	for i := range prev {
		prev[i] = minVal
	}

	for _, num1 := range nums1 {
		dp := make([]int, m+1)
		for k := range dp {
			dp[k] = minVal
		}

		for j, num2 := range nums2 {
			product := num1 * num2
			col := j + 1

			prevVal := prev[col-1]
			if prevVal < 0 {
				prevVal = 0
			}
			term1 := product + prevVal
			term2 := prev[col]
			term3 := dp[col-1]
			dp[col] = max(term1, max(term2, term3))
		}
		prev = dp
	}

	return prev[m]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
