class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        point2index = {}
        point2Pos = {}
        for i in range(n):
            point2index[score[i]] = i
        sortScore = score.copy()
        sortScore.sort(reverse=True)
        for i in range(n):
            point2Pos[sortScore[i]] = i+1
        
        ans = []
        for i in range(n):
            if point2Pos[score[i]] == 1 :
                ans.append("Gold Medal")
            elif point2Pos[score[i]] == 2 :
                ans.append("Silver Medal")
            elif point2Pos[score[i]] == 3 :
                ans.append("Bronze Medal")
            else :
                ans.append(str(point2Pos[score[i]]))
        return ans