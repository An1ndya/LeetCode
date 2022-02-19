import heapq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:  
        q = []
        mn=1000000000
        diff=1000000000
        for i in nums:
            if i%2==1:
                q.append(-i*2)
         
            else:
                q.append(-i)
  
        heapify(q)
        mn=-max(q)

        while True:
        
            v=-int(heappop(q))
         
            diff = min(diff,v-mn)
            if v%2==0:
                mn=min(int(v/2),mn)
                heappush(q, -int(v/2))
            else:
                diff=min(diff,v-mn)
                break

        return diff   
   