class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortheight = heights.copy()
        sortheight.sort()
        ans = 0
        for i in range(len(sortheight)):
            if sortheight[i] != heights[i]:
                ans += 1
        return ans