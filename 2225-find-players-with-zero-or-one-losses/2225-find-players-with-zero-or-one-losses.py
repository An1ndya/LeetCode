class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #loser to winer 
        win = defaultdict(int)
        loss = defaultdict(int)
        total = {}
        for pair in matches:
            win[pair[0]]+=1
            loss[pair[1]]+=1
            total[pair[0]]=True
            total[pair[1]]=True
        
        winnerlist = []
        oneloserList = []
        sortedlist = list(total.keys())
        sortedlist.sort()
        
        for player in sortedlist:
            if loss[player]==1:
                oneloserList.append(player)
            elif loss[player]==0 and win[player]>0:
                winnerlist.append(player)
                
        return [winnerlist,oneloserList]
            