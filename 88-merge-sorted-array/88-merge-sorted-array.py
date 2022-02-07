class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=m-1
        j=n-1
        end=m+n-1
        while end>-1:
            if i < 0:
                nums1[end]=nums2[j]
                j-=1
            elif j <0:
                nums1[end]=nums1[i]
                i-=1
            elif nums1[i]> nums2[j]:
                nums1[end]=nums1[i]
                i-=1
            else:
                nums1[end]=nums2[j]
                j-=1
            end-=1
        