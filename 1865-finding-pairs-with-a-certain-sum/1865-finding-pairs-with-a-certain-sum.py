from collections import Counter
class FindSumPairs:
    def __init__(self, nums1: list[int], nums2: list[int]):
        # store original arrays
        self.nums1 = nums1
        self.nums2 = nums2
        # build a counter of nums2 values for fast lookup
        self.count2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        """
        Increment nums2[index] by val, updating our Counter.
        """
        # old value
        old = self.nums2[index]
        # decrement its count
        self.count2[old] -= 1
        if self.count2[old] == 0:
            del self.count2[old]
        # update array
        new = old + val
        self.nums2[index] = new
        # increment new value count
        self.count2[new] += 1

    def count(self, tot: int) -> int:
        """
        Count how many pairs (i, j) satisfy nums1[i] + nums2[j] == tot.
        """
        ans = 0
        # for each value a in nums1, we need (tot - a) in nums2
        for a in self.nums1:
            need = tot - a
            ans += self.count2.get(need, 0)
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)