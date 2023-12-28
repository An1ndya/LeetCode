class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # finction with lru_cache 
        @lru_cache(None)
        def dfs(curindex, lastchar, consecutive, left2remove) :
            if left2remove < 0: 
                return 10000000
            if curindex>=len(s):
                return 0
            if s[curindex] == lastchar:
                #following consecutive+1 will result in increment of result
                #a-a2,a9-a10,a99-a100
                incrementdigitcount = 0
                if consecutive==99 or consecutive==9 or consecutive==1:
                    incrementdigitcount=1
                #take char, avoid del as every intial first sequential char already did it  
                return incrementdigitcount + dfs(curindex+1, lastchar, consecutive+1, left2remove)
            else:
                Len4keepcur = 1 + dfs(curindex+1, s[curindex], 1, left2remove)
                
                #delete cur char; passing consecutive result for previous sequence merge condtion
                Len4removecur = dfs(curindex+1, lastchar, consecutive, left2remove-1)
                
                return min(Len4keepcur,Len4removecur)
            
        return dfs(0,"",0, k)
                