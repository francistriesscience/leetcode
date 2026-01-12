package main

func minTimeToVisitAllPoints(points [][]int) int {
	if len(points) == 0 {
		return 0
	}

	totalTime := 0

	for i := 0; i < len(points)-1; i++ {
		p1 := points[i]
		p2 := points[i+1]

		dx := abs(p2[0] - p1[0])
		dy := abs(p2[1] - p1[1])

		totalTime += max(dx, dy)
	}

	return totalTime
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
