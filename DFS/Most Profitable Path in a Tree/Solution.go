func mostProfitablePath(edges [][]int, bob int, amount []int) int {
    // Build graph
    nodes := len(amount)
    graph := make(map[int][]int)

    // Initialize graph
    for i := 0; i < nodes; i++ {
        graph[i] = make([]int, 0)
    }

    // Build undirected graph
    for _, edge := range edges {
        a, b := edge[0], edge[1]
        graph[a] = append(graph[a], b)
        graph[b] = append(graph[b], a)
    }

    // Initialize bobPath and path
    bobPath := make([]int, nodes)
    for i := range bobPath {
        bobPath[i] = -1
    }
    path := []int{bob}

    // DFS to find Bob's path to root (0)
    var fillBobPath func(current, parent int) bool
    fillBobPath = func(current, parent int) bool {
        if current == 0 {
            return true
        }

        for _, nbr := range graph[current] {
            if nbr != parent {
                path = append(path, nbr)
                if fillBobPath(nbr, current) {
                    return true
                }
                path = path[:len(path)-1]
            }
        }
        return false
    }

    // Fill Bob's path
    fillBobPath(bob, -1)

    // Mark Bob's timing at each node
    for i, val := range path {
        bobPath[val] = i
    }

    // DFS to find Alice's maximum profit path
    var alicePath func(current, parent, currentTime int) int
    alicePath = func(current, parent, currentTime int) int {
        score := 0

        // Calculate score based on timing
        if bobPath[current] > currentTime || bobPath[current] == -1 {
            score = amount[current]
        } else if bobPath[current] == currentTime {
            score = amount[current] / 2
        }

        localMax := math.MinInt32
        wentIn := false

        // Explore all neighbors
        for _, nbr := range graph[current] {
            if nbr != parent {
                wentIn = true
                childScore := alicePath(nbr, current, currentTime+1)
                if childScore > localMax {
                    localMax = childScore
                }
            }
        }

        if wentIn {
            return score + localMax
        }
        return score
    }

    return alicePath(0, -1, 0)
}