package main

func canChange(start string, target string) bool {
	n := len(start)
	startPtr := 0
	targetPtr := 0

	for targetPtr < n {
		for targetPtr < n && target[targetPtr] == '_' {
			targetPtr++
		}

		for startPtr < n && start[startPtr] == '_' {
			startPtr++
		}

		if startPtr < n && targetPtr < n {
			if target[targetPtr] != start[startPtr] {
				return false
			}

			if target[targetPtr] == 'L' && startPtr < targetPtr {
				return false
			}

			if target[targetPtr] == 'R' && startPtr > targetPtr {
				return false
			}
		}

		startPtr++
		targetPtr++
	}

	return countChar(start, 'L') == countChar(target, 'L') && countChar(start, 'R') == countChar(target, 'R')
}

func countChar(s string, char rune) int {
	count := 0
	for _, c := range s {
		if c == char {
			count++
		}
	}
	return count
}
