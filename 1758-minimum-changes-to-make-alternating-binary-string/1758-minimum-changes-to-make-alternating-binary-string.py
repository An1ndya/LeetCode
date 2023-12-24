class Solution:
    def minOperations(self, s: str) -> int:
        n =len(s)
        #for two case 10.. or 01..
        op1,op2=0,0
        for i in range(n):
            if i%2==0:    
                if s[i]=='1':
                    op2+=1
                else:
                    op1+=1
            else:
                if s[i]=='1':
                    op1+=1
                else:
                    op2+=1
        return min(op1,op2)
                