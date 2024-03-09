class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1 =  len(nums1)
        n2 =  len(nums2)
        p1 = 0  # index in first list
        p2 = 0  #index in second list
        while p1 < n1 and p2 < n2:
            if nums1[p1] == nums2[p2]:
                #we found first coomon
                #as both list is sorted this should be minimum
                return nums1[p1]
            if nums1[p1] > nums2[p2]:
                #smaller p2 index of nums2 need to bigger for next check
                p2 += 1
            else:
                #smaller p1 index of nums1 need to bigger for next check
                p1 += 1
        #no common found so return -1
        return -1