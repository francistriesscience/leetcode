package main

func repeatedNTimes(nums []int) int {
	seen := make(map[int]struct{})

	for _, num := range nums {
		if _, exists := seen[num]; exists {
			return num
		}
		seen[num] = struct{}{}
	}

	return -1
}
