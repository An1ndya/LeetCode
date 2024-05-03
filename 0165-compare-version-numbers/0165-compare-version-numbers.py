class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        v1 = [int(v) for v in v1]
        v2 = [int(v) for v in v2]
        n1 = len(v1)
        n2 = len(v2)
        mx = max(n1,n2) # maximum revision count 
        #not satetd revision set as 0. so two sliding cause no issue
        for k in range(mx):
            if k >= n1:
                v1.append(0)
            if k >= n2:
                v2.append(0)
        i = 0
        j = 0
        #check for each revision
        while i<mx:
            if v1[i] < v2[j]:
                return -1
            elif v1[i] > v2[j]:
                return 1
            i+=1
            j+=1
     
        #only possible case is both are equal
        return 0