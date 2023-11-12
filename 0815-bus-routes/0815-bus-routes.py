class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target: return 0
        stopagetobus={}
        
        for bus in range(len(routes)):
            for stopage in routes[bus]:
                if stopage in stopagetobus:
                    stopagetobus[stopage].append(bus)
                else:
                    stopagetobus[stopage]=[bus]
        visited={}
        q=[]
        buscount=1
        for bus in stopagetobus[source]:
            q.append(bus)
            visited[bus]=True
                    
        while q:
            n=len(q)
            for i in range(n):
                bus=q.pop(0)
                for stopage in routes[bus]:
                    if stopage==target: return buscount
                    
                    for nextbus in stopagetobus[stopage]:
                        if not nextbus in visited:
                            q.append(nextbus)
                            visited[nextbus]=True
            buscount+=1
        return -1