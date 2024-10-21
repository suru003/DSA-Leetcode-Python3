package main
import (
	"fmt"
)

func maxUniqueSplit(s string) int {
	words := make(map[string]bool)  // To track unique substrings
	return recurse(s, 0, words)
}

func recurse(s string, index int, words map[string]bool) int {
	maxi := 0
	for i := index + 1; i <= len(s); i++ {
		tempWord := s[index:i]
		if !words[tempWord] {
			words[tempWord] = true
			maxi = max(maxi, 1+recurse(s, i, words))
			delete(words, tempWord)
		}
	}
	return maxi
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
