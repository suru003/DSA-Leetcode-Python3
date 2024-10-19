package main

import "fmt"

func findKthBit(n int, k int) byte {
	n--
	bits := []byte{'0'}

	for i := 1; i <= n; i++ {
		prevLength := len(bits)
		bits = append(bits, '1')

		for curIndex := prevLength - 1; curIndex >= 0; curIndex-- {
			if bits[curIndex] == '1' {
				bits = append(bits, '0')
			} else {
				bits = append(bits, '1')
			}
		}
	}

	return bits[k-1]
}
