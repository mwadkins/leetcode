def DFS (grid,r,c,visited):
        visited[r][c]=1
       	rows=len(grid)
	cols=len(grid[0])
        if (grid[r][c]=='1'):
                if ((r<rows-1) and (visited[r+1][c]==0)):
                        DFS(grid,r+1,c,visited)
                if ((r>0) and (visited[r-1][c]==0)):
                        DFS(grid,r-1,c,visited)
    	        if ((c<cols-1)  and (visited[r][c+1]==0)):
                        DFS(grid,r,c+1,visited)
                if ((c>0) and (visited[r][c-1]==0)):
                        DFS(grid,r,c-1,visited)


def islands (grid):
        print grid
	rows=len(grid)
	cols=len(grid[0])
        count=0
	visited = [[0 for c in range (cols)] for r in range (rows)]

	for r in range(rows):
		for c in range(cols):
			if ((grid[r][c]=='1') and (visited[r][c]==0)):
                                count+=1
				DFS(grid,r,c,visited)
        return count

c=islands(["11000","11000","00100","00011"])
print c
