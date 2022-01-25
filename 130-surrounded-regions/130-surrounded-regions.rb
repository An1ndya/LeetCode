# @param {Character[][]} board
# @return {Void} Do not return anything, modify board in-place instead.
def solve(board)
    m = board.length
    n = board[0].length
    isvisited = Array.new(m){Array.new(n,false)}
    
    for i in 0..m-1
        if board[i][0] == 'O' && !isvisited[i][0]
            DFS(board, i,0,m,n,isvisited)
        end
        if board[i][n-1] == 'O' && !isvisited[i][n-1]
            DFS(board, i,n-1,m,n,isvisited)
        end
    end
    for j in 0..n-1
        if board[0][j] == 'O' && !isvisited[0][j]
            DFS(board, 0,j,m,n,isvisited)
        end
        if board[m-1][j] == 'O' && !isvisited[m-1][j]
            DFS(board, m-1,j,m,n,isvisited)
        end
    end
    for i in 1..m-2
        for j in 1..n-2 
            if board[i][j] == 'O' && !isvisited[i][j]
                board[i][j] = 'X'
            end
        end
    end
    return board
end
def DFS(board,i,j,m,n,isvisited)
    
    if  i < 0 || i>m-1 || j <0 || j>n-1; return end
    
    if board[i][j] == 'O' && !isvisited[i][j]
        isvisited[i][j] = true
        DFS(board,i,j+1,m,n,isvisited)
        DFS(board,i,j-1,m,n,isvisited)
        DFS(board,i+1,j,m,n,isvisited)
        DFS(board,i-1,j,m,n,isvisited)
    end
end