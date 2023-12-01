import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        minheap =[(matrix[0][0],0,0)]
        heapq.heapify(minheap)
        val=0
        while minheap and k:
            val,row,col = heapq.heappop(minheap)
            #ans.append([nums1[i1],nums2[i2]])
            k-=1
            if row+1<n:
                heapq.heappush(minheap, (matrix[row+1][col],row+1,col))
            #avoid duplicate using row==0
            #other row!=0 values pair will come from traversing BFS
            if row==0 and  col+1<n:
                heapq.heappush(minheap, (matrix[row][col+1],row,col+1))    
        return val