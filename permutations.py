class Solution(object):
    def gen_palindromes (self,str,prefix):
        ret = []
        if (str==""):
            return [prefix]
        else:
            for i in range(len(str)):
                rem=str[:i] + str[i+1:]
                p = prefix + str[i]
                ret = ret + self.gen_palindromes(rem,p)
        return ret
                
    def palindrome (self,str):
        return self.gen_palindromes(str,"")

sol=Solution()
ret=sol.palindrome("walrus")
print ret
