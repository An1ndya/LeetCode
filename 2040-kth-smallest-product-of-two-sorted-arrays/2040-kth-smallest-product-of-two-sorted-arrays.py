import bisect
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def countLessEqual(x):
            count = 0
            for a in nums1:
                if a > 0:
                    count += bisect.bisect_right(nums2, x // a)
                elif a < 0:
                    count += len(nums2) - bisect.bisect_left(nums2, (x // a) + (x % a != 0))
                else:
                    if x >= 0:
                        count += len(nums2)
            return count

        left = -10**10
        right = 10**10

        while left < right:
            mid = (left + right) // 2
            if countLessEqual(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left