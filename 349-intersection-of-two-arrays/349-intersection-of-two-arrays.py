class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        n1=len(nums1)
        n2=len(nums2)
        nums1.sort()
        nums2.sort()
        i,j=0,0
        while i<n1 and j<n2:
            while i+1<n1 and nums1[i]==nums1[i+1]:i+=1 
            while j+1<n2 and nums2[j]==nums2[j+1]:j+=1 
            if nums1[i]==nums2[j]:
                ans.append(nums1[i])
                j+=1
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
        return ans