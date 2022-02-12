class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n=len(beginWord)
        d={}
        step=0
        for s in wordList:
            d[s]=True
            
        if endWord not in d: return 0
        
        q = []
        q.append(beginWord)
        while len(q) > 0:
            size = len(q)
            while size > 0:
                w=q.pop(0)
                if w == endWord:
                    return step+1
                for i in range(0,n):
                    c=w[i]
                    for j in range(26):
                        w = w[:i] + chr(ord('a')+j) + w[i + 1:]
                        if w in d and d[w]:
                            q.append(w)
                            d[w] = False             
                    w = w[:i] + c + w[i + 1:]
                size-=1
            step+=1
        return 0
            
        