package main

import (
    "container/heap"
    "fmt"
    "math"
)

// A Node represents a position in the grid and the time at which it is reached.
type Node struct {
    i, j  int
    time  int
}

// A PriorityQueue implements heap.Interface and holds Nodes.
type PriorityQueue []*Node

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(a, b int) bool {
    // We want Pop to give us the node with the smallest time.
    return pq[a].time < pq[b].time
}

func (pq PriorityQueue) Swap(a, b int) {
    pq[a], pq[b] = pq[b], pq[a]
}

func (pq *PriorityQueue) Push(x interface{}) {
    *pq = append(*pq, x.(*Node))
}

func (pq *PriorityQueue) Pop() interface{} {
    old := *pq
    n := len(old)
    node := old[n-1]
    *pq = old[0 : n-1]
    return node
}

// minTimeToExit returns the minimum time to reach (n-1, m-1) from (0,0)
// given moveTime constraints.
func minTimeToReach(moveTime [][]int) int {
    n, m := len(moveTime), len(moveTime[0])
    // Directions: down, up, right, left
    dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

    // dist[i][j] = best known earliest arrival time at (i,j)
    dist := make([][]int, n)
    for i := range dist {
        dist[i] = make([]int, m)
        for j := range dist[i] {
            dist[i][j] = math.MaxInt32
        }
    }
    dist[0][0] = 0

    // Initialize priority queue with the start node.
    pq := &PriorityQueue{&Node{0, 0, 0}}
    heap.Init(pq)

    for pq.Len() > 0 {
        node := heap.Pop(pq).(*Node)
        t, i, j := node.time, node.i, node.j

        // If this popped time is worse than a previously found path, skip it.
        if t > dist[i][j] {
            continue
        }
        // If we've reached the goal, this is the optimal time.
        if i == n-1 && j == m-1 {
            return t
        }

        // Relax each neighbor.
        for _, d := range dirs {
            ni, nj := i+d[0], j+d[1]
            if ni >= 0 && ni < n && nj >= 0 && nj < m {
                // You can't enter (ni,nj) until moveTime[ni][nj], then +1 second to move.
                wait := moveTime[ni][nj]
                if t < wait {
                    t = wait
                }
                nt := t + 1
                if nt < dist[ni][nj] {
                    dist[ni][nj] = nt
                    heap.Push(pq, &Node{ni, nj, nt})
                }
                // Restore t for next neighbor
                t = node.time
            }
        }
    }

    // If unreachable (shouldn't happen in a valid dungeon), return -1.
    return -1
}

