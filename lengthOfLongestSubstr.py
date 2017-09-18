class Solution(object):
    def lengthOfLongestSubstring(self, s,exp):
        """
        :type s: str
        :rtype: int
        """
        print "s=",s

        count=0
        my_max=0
        substr=""
        dict={}
        start=0
        stop=0
        count=0
        ret=""
        my_ret=""
        curr=0
        end=len(s)-1        
    
        while curr<=end:
            c=s[curr]
            print c
            if c in dict:
                curr=dict[c]+1
                #reset
		dict={}
                #print "ret=",ret
                ret=""
                count=0
	    else:
            	dict[c]=curr
            	ret = ret + c
            	count+=1
            	curr+=1
            if (count>my_max):
                my_max=count
                my_ret=ret
            
        print "ret=",my_ret," max=",my_max
        if (my_max != exp):
            print "FAILED"
        return my_max
    


sol=Solution()

s="abcabcbb"
m=sol.lengthOfLongestSubstring(s,3)


s="bbbbb"
m=sol.lengthOfLongestSubstring(s,1)


s="pwwkew"
m=sol.lengthOfLongestSubstring(s,3)

s="c"
m=sol.lengthOfLongestSubstring(s,1)

s=""
m=sol.lengthOfLongestSubstring(s,0)


s="dvdf"
m=sol.lengthOfLongestSubstring(s,3)


