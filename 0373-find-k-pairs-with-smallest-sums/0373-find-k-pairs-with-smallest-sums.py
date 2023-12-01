import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans =[]
        n1=len(nums1)
        n2=len(nums2)
        minheap = [(nums1[0]+nums2[0],0,0)]
        heapq.heapify(minheap)
        while minheap and k:
            sm,i1,i2 = heapq.heappop(minheap)
            ans.append([nums1[i1],nums2[i2]])
            k-=1
            if i1+1<n1:
                heapq.heappush(minheap, (nums1[i1+1]+nums2[i2],i1+1,i2))
            #avoid duplicate using i1==0
            #other i1!=0 values pair will come from traversing BFS
            
            if i1==0 and  i2+1<n2:
                heapq.heappush(minheap, (nums1[i1]+nums2[i2+1],i1,i2+1))    
        return ans