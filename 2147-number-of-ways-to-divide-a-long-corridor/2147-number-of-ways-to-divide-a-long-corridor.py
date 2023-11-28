class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n=len(corridor)
        totalS=0
        ways=1
        evenSindex=-1
    
        for i in range(n):
            if corridor[i]=='S':
                totalS+=1
                if totalS%2==0 and totalS!=0:
                    evenSindex=i
                elif totalS%2==1 and totalS>2:
                    ways*=i-evenSindex
                    ways%=1000000007
        if totalS%2==1 or totalS==0: 
            return 0
        return ways
                