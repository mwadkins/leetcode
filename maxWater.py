class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a=0
        l=0
        r=len(height)-1
        done=False
        while (l<r):
                area=min(height[l],height[r])*(r-l)
		print "a[",l,"]=",height[l],"a[",r,"]=",height[r]," area=",area 
                if (area>a):
                    a=area
                if (height[l]<height[r]):
                   l+=1
                else:
                   r-=1 
        return a

sol=Solution()
r=sol.maxArea([2,3,10,5,7,8,9])
print r
