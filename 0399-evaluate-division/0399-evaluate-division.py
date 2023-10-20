class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ans=[]
        graph = {}
        n =len(equations)
        for i in range(n):
            
            if equations[i][0] not in graph:
                graph[equations[i][0]]=[]
            if equations[i][1] not in graph:
                graph[equations[i][1]]=[]
                
            graph[equations[i][0]].append([equations[i][1],values[i]])
            graph[equations[i][1]].append([equations[i][0],1/values[i]])
        for q in queries:
            if q[0] not in graph or  q[1] not in graph:
                ans.append(-1.0000)
                continue
            if q[0] == q[1] :
                ans.append(1.0000)
                continue
            queue = [[q[0],1]]
            visited = set()
            found = False
            while queue:
                node = queue.pop(0)
                if node[0] == q[1]: 
                    found = True
                    ans.append(node[1])
                    break
                for child in graph[node[0]]:

                    if child[0] not in visited:
                        visited.add(child[0])
                        queue.append([child[0],child[1]*node[1]])
                        
            if not found: ans.append(-1.0000)
        return ans