class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()
        for num in arr:
            new_cur = {num}
            for prev in cur:
                new_cur.add(prev | num)
            cur = new_cur
            res.update(cur)
        return len(res)