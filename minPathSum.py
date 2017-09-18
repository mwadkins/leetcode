class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_rows=len(grid)
        num_cols=len(grid[0])

        sums=grid
        #sums = [[0 for c in range (num_cols)] for r in range (num_rows)]
        # handle boundaries
        for c in range (1,num_cols):
            sums[0][c]=sums[0][c]+sums[0][c-1]
        for r in range (1,num_rows):
            sums[r][0]=sums[r][0]+sums[r-1][0]
        print sums
        for r in range (1,num_rows):
            for c in range (1,num_cols):
                (up,left) = (0,0)
                up=sums[r-1][c]
                left=sums[r][c-1]
                sums[r][c] = sums[r][c]+min(up,left)
		print "set [",r,"][",c,"] to ",grid[r][c]
        print sums
        return sums[num_rows-1][num_cols-1]

sol=Solution()
r=sol.minPathSum([[1,2],[1,1]])
print r
