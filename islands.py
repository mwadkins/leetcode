class Solution(object):
    def DFS (self,grid,row,col,visited):
        
        # recur for all connected neighbors
        visited[row][col]=1

        num_rows=len(grid)
        num_cols=len(grid[0])
        
        if (grid[row][col]=='1'):
            # up
            if ((row>0) and (visited[row-1][col]==0)):
                self.DFS(grid,row-1,col,visited)
            # down
            if ((row<num_rows-1) and (visited[row+1][col]==0)):
                self.DFS(grid,row+1,col,visited)
            # left
            if ((col>0) and (visited[row][col-1]==0)):
                self.DFS(grid,row,col-1,visited)
            # right
            if ((col < num_cols-1) and (visited[row][col+1]==0)):
                self.DFS(grid,row,col+1,visited)
            
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count=0
        print grid
        # mark all nodes as not visited
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range (len(grid)):
            for j in range (len(grid[i])):
                if ((grid[i][j]=='1') and (visited[i][j]==0)):
                    # new island
                    count+=1
                    self.DFS(grid,i,j,visited)
        return count

sol=Solution()
#c=sol.numIslands(["11110","11010","11000","00000"])

c=sol.numIslands(["11000","11000","00100","00011"])
print c 
