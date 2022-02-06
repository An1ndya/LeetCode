class Solution:

    def __init__(self, nums: List[int]):
        self.org=nums.copy()
        self.s=nums.copy()

    def reset(self) -> List[int]:
        self.s=self.org.copy()
        return self.org

    def shuffle(self) -> List[int]:
        random.shuffle(self.s)
        return self.s


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()