class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        curr_len=len(nums)
        if (curr_len<2):
            return curr_len
        
        for i in range (1,len(nums)-1):
            if (i>curr_len-1):
                break
            while ((nums[i+1]==nums[i]) and (i<curr_len-1)):
	        print "i=",i," nums=",nums
                # duplicate
                # swap until you get to end
                curr_len-=1
                for j in range (i,curr_len-1):
                    nums[j+1]=nums[j+2]
	        #write the duplicate at the end
	        nums[len(nums)-1]=nums[i]
	print nums                    
        return curr_len

sol=Solution()
#c=sol.removeDuplicates([1,2,3,3,4,4,4,5,6,6,7,7])
#print c


c=sol.removeDuplicates([1,2,3,3,3,4,5,6])
print c
