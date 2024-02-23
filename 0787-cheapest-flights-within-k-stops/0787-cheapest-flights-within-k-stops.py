class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for cost in flights:
            #source, to , price = cost[0], cost[1], cost[2]  
            graph[cost[0]].append((cost[1],cost[2]))
        #total cost from source city 
        cost = [float('inf')] * n
        cost[src] = 0
        pq = []
        pq.append((0, src))
        stopscount = 0
        while pq:
            # break if stopcount more than k
            if stopscount > k : break
            
            p = len(pq)
            
            for i in range(p):
                #totalcost, city  = heapq.heappop(pq)
                totalcost, city  =  pq.pop(0)
                for neighbour, weight in graph[city]:
                    # If there is shorted path to neighbour through city.
                    if cost[neighbour] > totalcost + weight:
                        # Updating distance of neighbour
                        cost[neighbour] = totalcost + weight
                        pq.append((cost[neighbour], neighbour))
            stopscount+=1
            
        if cost[dst] < float('inf'):
            #distance updated, so stopcount less than k
            return cost[dst]
        else:
            #did not make to dst with k stopcount 
            return -1