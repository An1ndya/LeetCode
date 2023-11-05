class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n=len(arr)
        wincount=0
        mx=0
        for i in arr:
            mx=max(i,mx)
            
        if k >= n: return mx
        curmax=arr[0]
    
        for i in arr[1:]:
            if curmax>i:
                wincount+=1
            else:
                curmax=i
                wincount=1
                
        
            if wincount==k or curmax==mx:
                return curmax
        return -1
            
            