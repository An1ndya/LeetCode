class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #consider like a graph
        indegree = defaultdict(int)  #how many trust i th man
        outdegree = defaultdict(int)  #How many are trusted by i th man 
        for trustpair in trust:
            #increase trustee
            indegree[trustpair[1]]+=1
            #increase trusted person
            outdegree[trustpair[0]]+=1
        for i in range(1,n+1):
            #all except i trust i and i dont trust anyone
            if indegree[i]==n-1 and outdegree[i] == 0:
                return i
        return -1