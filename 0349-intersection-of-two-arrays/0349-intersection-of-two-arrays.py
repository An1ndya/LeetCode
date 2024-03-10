class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        n1=len(nums1)
        n2=len(nums2)
        #sort arrays
        nums1.sort()
        nums2.sort()
        i,j=0,0 #index of two arrays
        while i<n1 and j<n2:
            #skip redundant equal number 
            while i+1<n1 and nums1[i]==nums1[i+1]:i+=1 
            while j+1<n2 and nums2[j]==nums2[j+1]:j+=1 
            # common so add to answer list  
            if nums1[i]==nums2[j]:
                ans.append(nums1[i])
                #next elemnts for both of them
                j+=1
                i+=1
            elif nums1[i]>nums2[j]:
                #num2 is smaller, so take its next
                j+=1
            elif nums1[i]<nums2[j]:
                #num1 is smaller, so take its next
                i+=1
        return ans