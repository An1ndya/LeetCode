class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        isvisited=[False]*len(arr)
        return self.DFS(arr,start,isvisited)
    
    def DFS(self,arr,i,isvisited) -> bool:
        
        if i > len(arr)-1 or i <0: return False
        if isvisited[i] : return False
        if arr[i] == 0 : return True
        isvisited[i] = True
        return self.DFS(arr,i+arr[i],isvisited ) or self.DFS(arr,i-arr[i],isvisited )