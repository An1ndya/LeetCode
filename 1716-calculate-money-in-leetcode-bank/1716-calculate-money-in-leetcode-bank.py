class Solution:
    def totalMoney(self, n: int) -> int:
        totalsave=0
        w=n//7
        if w >= 1:
            firstweek = 28
            lastweek  = 28 + 7*(w-1)
            totalsave+= (firstweek+lastweek)*w//2
            
        dayonlastweek = n%7
        firstdayonlastweek =w+1
        lastdayonlastweek  = firstdayonlastweek+dayonlastweek-1
         
        totalsave+=(firstdayonlastweek+lastdayonlastweek)*(dayonlastweek)//2
        return totalsave
        
        