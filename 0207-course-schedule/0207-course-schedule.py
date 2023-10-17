class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        visited = [0 for i in range(numCourses)]
        for p in prerequisites:
            graph[p[1]].append(p[0])
            
        def DFS(c):
            if visited[c]==1: return True
            if visited[c]==-1: return False
            
            visited[c]=-1
            for child in graph[c]:
                if DFS(child) == False: return False
            visited[c]=1
            
        for c in range(numCourses):
                if DFS(c) == False: return False
        return True