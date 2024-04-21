class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for i in range(n)]
        visited =[False]*n
        #create adjacency list
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        queue = deque([source])
        #BFS
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node == destination:
                    return True 
                visited[node] = True
                for child in graph[node]:
                    if not visited[child]:
                        queue.append(child)
        return False