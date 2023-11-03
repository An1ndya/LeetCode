class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        tn=len(target)
        ans=[]
        indexoftarget=0
        for i in range(1,n+1):
            if indexoftarget ==tn: break
            
            if i == target[indexoftarget]:
                ans.append("Push")
                indexoftarget+=1
            elif i < target[indexoftarget]:
                ans.append("Push")
                ans.append("Pop")
        return ans        