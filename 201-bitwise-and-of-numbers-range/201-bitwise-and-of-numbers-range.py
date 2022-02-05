class Solution:
    
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        bitc=0
        while left!=right:
            left = left >>1
            right = right >>1
            bitc+=1
        return right<<bitc