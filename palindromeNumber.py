class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ret=False
        
        if (x<0):
            return False
        revertedNumber=0
        num=x
        while(num):
            revertedNumber=revertedNumber*10+num%10
            num=num/10
        if (revertedNumber == x):
            ret=True
        return ret


sol=Solution()
sol.isPalindrome(3223)
