"""
Was asked the following question during my onsite. Ran out of time before forming a full solution, still not sure what a good approach to this would be.

Given on-call rotation schedule for multiple people by: their name, start time and end time of the rotation:

Abby 1 10
Ben 5 7
Carla 6 12
David 15 17

Your goal is to return rotation table without overlapping periods representing who is on call during that time. Return "Start time", "End time" and list of on-call people:

1 5 Abby
5 6 Abby, Ben
6 7 Abby, Ben, Carla
7 10 Abby, Carla
10 12 Carla
"""
import heapq as hq


def solution(schedule):
    start_heap = []
    end_heap = []
    end_time = 0

    for start, end, name in schedule:
        hq.heappush(start_heap, [start, end, name])
        end_time = max(end_time, end)

    cur = 0
    # assuming no duplicated names
    in_meeting = set()
    answer = []

    while cur < end_time:
        nex = end_time
        if start_heap:
            nex = min(nex, start_heap[0][0])
        if end_heap:
            nex = min(nex, end_heap[0][0])

        if in_meeting:
            answer.append([cur, nex, list(in_meeting)])

        cur = nex

        while start_heap and start_heap[0][0] == cur:
            temp = hq.heappop(start_heap)
            hq.heappush(end_heap, [temp[1], temp[2]])
            in_meeting.add(temp[2])

        while end_heap and cur >= end_heap[0][0]:
            in_meeting.remove(hq.heappop(end_heap)[1])

    return answer


schedule = [[1, 10, "Abby"], [5, 7, "Ben"], [6, 12, "Carla"], [15, 17, "David"]]
table = solution(schedule)

for row in table:
    print(row)

