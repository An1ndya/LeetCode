import heapq
class Graph:
    #self.n=0
    #self.adjList=None
    def __init__(self, n: int, edges: List[List[int]]):
        self.n=n
        self.adjList=[[] for i in range(n)]
        self.edgecosthash={}
        for edge in edges:
            self.addEdge(edge)
        print(self.adjList)
    def addEdge(self, edge: List[int]) -> None:
        self.adjList[edge[0]].append(edge[1])
        self.edgecosthash[str(edge[0])+"->"+str(edge[1])]=edge[2]
        return

    def shortestPath(self, node1: int, node2: int) -> int:

        pq = []
        heapq.heappush(pq, (0,node1))
        dist = [1000000000] * self.n
        dist[node1] = 0
 
        while pq:

            d, u = heapq.heappop(pq)
            #we always push min dis first so first node2 will have min distance 
            if u==node2: return d
            for v in self.adjList[u]:
                # If there is shorted path to v through u.
                weight = self.edgecosthash[str(u)+"->"+str(v)]
                if dist[v] > dist[u] + weight:
                    # Updating distance of v
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v],v))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)