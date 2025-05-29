func maxTargetNodes(edges1 [][]int, edges2 [][]int) []int {
	n, m := len(edges1)+1, len(edges2)+1

	graph1 := make([][]int, n)
	graph2 := make([][]int, m)
	for _, e := range edges1 {
		graph1[e[0]] = append(graph1[e[0]], e[1])
		graph1[e[1]] = append(graph1[e[1]], e[0])
	}
	for _, e := range edges2 {
		graph2[e[0]] = append(graph2[e[0]], e[1])
		graph2[e[1]] = append(graph2[e[1]], e[0])
	}

	// Single BFS from node 0 in Tree2
	maxOdd2 := getMaxOddCount(graph2)

	// Precompute even/odd count for Tree1 using rerooting DP
	even := make([]int, n)
	odd := make([]int, n)
	visited := make([]bool, n)
	dfsCount(graph1, 0, -1, even, odd, visited)

	answer := make([]int, n)
	visited2 := make([]bool, n)
	reroot(graph1, 0, -1, even, odd, visited2, maxOdd2, answer)

	return answer
}

func getMaxOddCount(graph [][]int) int {
	n := len(graph)
	colors := make([]int, n)
	for i := range colors {
		colors[i] = -1
	}
	queue := []int{0}
	colors[0] = 0
	count := [2]int{1, 0}

	for len(queue) > 0 {
		u := queue[0]
		queue = queue[1:]

		for _, v := range graph[u] {
			if colors[v] == -1 {
				colors[v] = 1 - colors[u]
				count[colors[v]]++
				queue = append(queue, v)
			}
		}
	}
	if count[0] > count[1] {
		return count[0]
	}
	return count[1]
}


func dfsCount(graph [][]int, u, parent int, even, odd []int, visited []bool) {
	visited[u] = true
	even[u] = 1
	for _, v := range graph[u] {
		if v != parent {
			dfsCount(graph, v, u, even, odd, visited)
			even[u] += odd[v]
			odd[u] += even[v]
		}
	}
}

func reroot(graph [][]int, u, parent int, even, odd []int, visited []bool, maxOdd2 int, answer []int) {
	visited[u] = true
	answer[u] = even[u] + maxOdd2

	for _, v := range graph[u] {
		if v != parent {
			// Backup counts
			eu, ou := even[u], odd[u]
			ev, ov := even[v], odd[v]

			// Remove v's contribution from u
			even[u] -= odd[v]
			odd[u] -= even[v]

			// Add u's contribution to v
			even[v] += odd[u]
			odd[v] += even[u]

			reroot(graph, v, u, even, odd, visited, maxOdd2, answer)

			// Restore counts
			even[u], odd[u] = eu, ou
			even[v], odd[v] = ev, ov
		}
	}
}
