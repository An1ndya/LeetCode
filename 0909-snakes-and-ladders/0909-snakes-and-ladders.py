class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        q=[1]
        ans=0
        n=len(board)
        visited = [False for i in range(n*n+1)]
        while q:
            #print(q)
            levelsize=len(q)
            for k in range(levelsize):
                node=q.pop(0)
                #print(node)
                r=(node-1)//n
                c=(node-1)%n
                if r%2!=0: 
                    c=n-1-c
                r=n-1-r
                #print(r,c)
                if board[r][c]!=-1:
                    node=board[r][c]
                if node>=n*n: return ans
                
                for i in range(1,7):
                    if node+i<=n*n and not visited[node+i]:
                        visited[node+i] = True
                        q.append(node+i)
            ans +=1
        return -1