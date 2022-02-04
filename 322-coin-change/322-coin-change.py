class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        
        d=0
        q = []
        q.append(0)
        v =[False]*(amount+1)
        
        while(q):
            size=len(q)
            for i in range(size):
                s=q.pop(0)
                if s > amount:continue
                if s==amount: return d
                if v[s] :continue
                if s<amount:
                    for j in coins:
                        q.append(s+j)
                v[s] = True
            d+=1
                    
        return -1 
   