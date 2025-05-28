func maxTargetNodes(edges1 [][]int, edges2 [][]int, k int) []int {
    n := len(edges1) + 1
	m := len(edges2) + 1

	// Build adjacency list for Tree1
	g1 := make([][]int, n)
	for _, e := range edges1 {
		u, v := e[0], e[1]
		g1[u] = append(g1[u], v)
		g1[v] = append(g1[v], u)
	}

	// Build adjacency list for Tree2
	g2 := make([][]int, m)
	for _, e := range edges2 {
		u, v := e[0], e[1]
		g2[u] = append(g2[u], v)
		g2[v] = append(g2[v], u)
	}

	// Precompute number of target nodes within distance k in Tree1 for each node
	answer := make([]int, n)
	for i := 0; i < n; i++ {
		count1 := countWithinK(g1, i, k)
		answer[i] = count1
	}

	// Precompute maximum number of target nodes within distance (k-1) in Tree2
	maxCount2 := 0
	for i := 0; i < m; i++ {
		count2 := countWithinK(g2, i, k-1)
		if count2 > maxCount2 {
			maxCount2 = count2
		}
	}

	// Add maxCount2 to each answer[i]
	for i := 0; i < n; i++ {
		answer[i] += maxCount2
	}

	return answer
}


func countWithinK(graph [][]int, start int, k int) int {
	n := len(graph)
	visited := make([]bool, n)
	q := list.New()
	q.PushBack([2]int{start, 0})
	visited[start] = true
	count := 0

	for q.Len() > 0 {
		front := q.Remove(q.Front()).([2]int)
		u, dist := front[0], front[1]

		if dist > k {
			continue
		}
		count++

		for _, v := range graph[u] {
			if !visited[v] {
				visited[v] = true
				q.PushBack([2]int{v, dist + 1})
			}
		}
	}
	return count
}

