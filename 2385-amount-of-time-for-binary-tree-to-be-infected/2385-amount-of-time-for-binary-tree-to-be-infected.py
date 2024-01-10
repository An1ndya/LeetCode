# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        minute = -1
        graph = defaultdict(list)
        def DFS(root, parent):
            if not root: return
            
            if parent: graph[root.val].append(parent.val)
            
            if root.left: 
                graph[root.val].append(root.left.val)
                DFS(root.left, root)
            if root.right: 
                graph[root.val].append(root.right.val)
                DFS(root.right, root)
        DFS(root, None)
        #print(graph)
        #BFS
        queue = [start]
        visited = defaultdict(bool)
        while len(queue)>0:
            n=len(queue)
            for i in range(n):
                node = queue.pop(0)
                visited[node]= True
                for child in graph[node]:
                    if not visited[child]:
                        queue.append(child)
            minute+=1
            #print(queue,minute)
        return minute
                