class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n=len(adjacentPairs)
        hashmap={}
        first=0
        for pair in adjacentPairs:
            p1=pair[0]
            p2=pair[1]
            if p1 in hashmap:
                hashmap[p1].append(p2)
            else:
                hashmap[p1]=[p2]
            if p2 in hashmap:
                hashmap[p2].append(p1)
            else:
                hashmap[p2]=[p1]
        for key in hashmap:
            if len(hashmap[key])==1:
                first =key
                break
        #print(hashmap)
        #print(first)
        
        prev =first
        cur=hashmap[first][0]
        ans=[first,cur]
        while n>1:
            #print(cur)
            nextn=hashmap[cur][0]+hashmap[cur][1]-prev
            
            prev=cur
            cur =nextn
            ans.append(cur)
            n-=1
        return ans
            