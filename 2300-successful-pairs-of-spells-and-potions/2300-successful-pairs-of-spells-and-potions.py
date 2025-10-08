import bisect
import math
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        res = []

        for s in spells:
            need = math.ceil(success / s)
            idx = bisect.bisect_left(potions, need)
            res.append(m - idx)
        
        return res