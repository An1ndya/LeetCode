# @param {Integer[][]} grid
# @return {Integer}
def shortest_path_binary_matrix(grid)
    n = grid.length
    isvisited = Array.new(n){Array.new(n,false)}
    
    if grid[0][0] == 1 || grid[n-1][n-1]==1; return -1 end
    
    dir = [[+1,+1,+1,-1,-1,-1,+0,+0],
           [+1,+0,-1,+1,+0,-1,+1,-1]]
    
    dis = 1
    queue = Queue.new
    queue.push([0,0])
    isvisited[0][0] =  true
    
    until queue.empty? do
    
        size = queue.length
        
        while size > 0
            
            node = queue.pop 
            
            if node[0]==n-1 && node[1]==n-1;
                return dis
            end
            
            for i in 0..7
                x = node[0]+dir[0][i]
                y = node[1]+dir[1][i]
                if x >=0 && x<n && y >=0 && y<n
                    if grid[x][y] == 0 && !isvisited[x][y]
                        queue.push([x,y])
                        isvisited[x][y] =  true
                    end
                end
            end
            size -=1
        end
        dis += 1
    end
    return -1    
end