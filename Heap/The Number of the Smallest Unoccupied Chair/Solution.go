import (
	"container/heap"
	"sort"
)

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

// Fields order is important because of memory alignment for structs.
// You can change the order and check the updated size of the struct.
type action struct {
	time      int32
	friend    int16
	isLeaving bool
}

// Time complexity: O(NlogN),
// Space complexity: O(N),
// where N - number of friends.
func smallestChair(times [][]int, targetFriend int) int {
	actions := make([]action, 0, 2*len(times))
	for i := range times {
		time := times[i]
		arrAct := action{
			friend:    int16(i),
			time:      int32(time[0]),
			isLeaving: false,
		}
		leavAct := action{
			friend:    int16(i),
			time:      int32(time[1]),
			isLeaving: true,
		}
		actions = append(actions, arrAct, leavAct)
	}

	sort.Slice(actions, func(i, j int) bool {
		if actions[i].time != actions[j].time {
			return actions[i].time < actions[j].time
		}
		return actions[i].isLeaving
	})

	freeChairs := &IntHeap{0}
	heap.Init(freeChairs)

	frndChair := make([]int, len(times))
	for _, act := range actions {
		if act.friend == int16(targetFriend) {
			break
		}

		if act.isLeaving {
			chair := frndChair[act.friend]
			heap.Push(freeChairs, chair)
		} else {
			chair := (heap.Pop(freeChairs)).(int)
			frndChair[act.friend] = chair

			if freeChairs.Len() == 0 {
				heap.Push(freeChairs, chair+1)
			}
		}
	}
	return (heap.Pop(freeChairs)).(int)
}