class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            colmap, rowmap, gridmap={},{},{}
            "p,q = 3*int(i/3), (i%3)*3"
            for j in range(0,9):
                
                r=board[i][j]
                if r!='.' :
                    if r in rowmap:
                        return False
                    rowmap[r]=True
                    
                c=board[j][i]
                if c!='.' :
                    if c in colmap:
                        return False
                    colmap[c]=True
                
                "g=board[p][q]"
                g=board[3*int(i/3)+int(j/3)][(i%3)*3+j%3]
                if g!='.' :
                    if g in gridmap:
                        return False
                    gridmap[g]=True
                """
                q+=1
                if q%3==0:
                    p+=1
                    q=(i%3)*3
                """
                    
        return True