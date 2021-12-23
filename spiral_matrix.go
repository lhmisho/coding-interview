package main

import "fmt"

func spiralOrder(A [][]int) []int {
	m := len(A)
	n := len(A[0])
	left := 0
	right := n - 1
	top := 0
	bottom := m - 1

	result := make([]int, m*n)

	direction := 0
	index := 0
	var i int

	for top <= bottom && left <= right {
		if direction == 0 {
			for i = left; i <= right; i++ {
				result[index] = A[top][i]
				index++
			}
			top++
		} else if direction == 1 {
			for i = top; i <= bottom; i++ {
				result[index] = A[i][right]
				index++
			}
			right--
		} else if direction == 2 {
			for i = right; i >= left; i-- {
				result[index] = A[bottom][i]
				index++
			}
			bottom--
		} else {
			fmt.Println()
			for i = bottom; i >= top; i-- {
				result[index] = A[i][left]
				index++
			}
			left++
		}
		direction = (direction + 1) % 4

	}
	return result
}

func main() {

	matrix := [][]int{
		{1, 2, 3, 4},
		{12, 13, 14, 5},
		{11, 16, 15, 6},
		{10, 9, 8, 7},
	}

	ss := spiralOrder(matrix)
	fmt.Println(ss)
}
