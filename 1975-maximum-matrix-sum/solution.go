package main

import "math"

func maxMatrixSum(matrix [][]int) int64 {
	var totalSum int64 = 0
	minAbsVal := int64(math.MaxInt64)
	negativeCount := 0

	for _, row := range matrix {
		for _, val := range row {
			absVal := int64(val)
			if absVal < 0 {
				absVal = -absVal
			}

			totalSum += absVal

			if val < 0 {
				negativeCount++
			}

			if absVal < minAbsVal {
				minAbsVal = absVal
			}
		}
	}

	if negativeCount%2 == 0 {
		return totalSum
	}

	return totalSum - 2*minAbsVal
}
