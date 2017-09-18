class Solution(object):
    def expand (self,l,r,s):
        left=l
        right=r
        while ((left>=0) and (right<len(s)) and (s[right]==s[left])):
            right+=1
            left-=1
        # subtract 1 bc we go one too far
        return right-left-1

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left=0
        right=0
        max_len=1
        pivot=0
        for i in range (len (s)):
            l1=self.expand(i,i,s)
            l2=self.expand(i,i+1,s)
            l=max(l1,l2)
            if (l>max_len):
                max_len=l
                pivot=i
        left=pivot-(max_len-1)/2
        right=pivot+max_len/2
        p=s[left:right+1]
        print "input=",s," p=",p," l=",left," r=",right," pivot=",pivot," max_len=",max_len

sol=Solution()
sol.longestPalindrome("abereab")
sol.longestPalindrome("a")
sol.longestPalindrome("aa")
sol.longestPalindrome("aaa")
sol.longestPalindrome("caabbaad")
