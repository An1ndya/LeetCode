class Solution:
    
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        #how many last bits have 0
        bitc=0
        while left!=right:
            #check from last bit of each
            #As they not equal means current checked last bit 0 in answer
            left = left >>1
            right = right >>1
            bitc+=1
        #when both left and right equal
        #then remaining bits will stay same
        #101pq & 101xy all numbers between them have 101 with those position
        #so there AND return 10100 in that postion
        #set last 0 bit count bitc  
        return right<<bitc