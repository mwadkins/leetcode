class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

	p=x
	res=0
	neg=False
	if (p<0):
		neg=True
		p=0-p
	while(p):
		mod=p%10
		p=p/10
		res=res*10+mod
	if (res>=0x80000000):
		return 0
	if (neg):
		res=0-res
	return res

sol = Solution()

n=123
s = sol.reverse(n)
print "n=",n,", s=",s

n=0x1
s = sol.reverse(n)
print "n=",n,", s=",s


n=-123
s = sol.reverse(n)
print "n=",n,", s=",s


n=1534236469
s = sol.reverse(n)
print "n=",n,", s=",s


