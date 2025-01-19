"""
Give an array of numbers of size n, pick a group of size m, find the kth minimum element in that group.

Example:

arr = [1, 3, 2, 1], m = 3, k = 2
m represents a group size
k represents the kth minimum element in the group of size m
so find the 2nd minimum element in a group of size 3.

There are 2 contiguous groups possible:
[1, 3, 2] and [3, 2, 1]

k = 2 , 2nd minimum element in above groups is [2,2]
Constraints:

k, m , n are of size 1 to 10^5
array item is of size 1 to 10^9
"""
from sortedcontainers import SortedList

def solution(arr, m, k):
    answer = []
    window = SortedList()

    for index, val in enumerate(arr):
        window.add(val)

        if index >= m:
            window.remove(arr[index - m])

        if index >= m - 1:
            answer.append(window[k - 1])

    return answer


arr = [1, 3, 2, 1]
m, k = 3, 2
print(f'Case 1: {solution(arr, m, k)}')

arr = [67, 225, 134, 28, 225, 152, 10, 128, 59]
m, k = 5, 3
print(f'Case 2: {solution(arr, m, k)}')