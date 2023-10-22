class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        hash={}
    
        for i in bank:
            hash[i]=False
        hash[startGene] = False
        
        move=0
        
        q=[startGene]
        while q:
            n=len(q)
            for i in range(n):
                cur=q.pop(0)
                #print(cur)
                #print(q)
                del hash[cur]
                if cur==endGene: return move
                for j in range(len(cur)):
                    char= "ACGT"
                    for k in range(4):
                        if cur[j]!=char[k]: 
                            child = cur[:j] + char[k] +cur[j+1:]
                            if child in hash:     
                                if hash[child] == False: 
                                    q.append(child) 
                                hash[child]=True
            move+=1  
        return -1
        