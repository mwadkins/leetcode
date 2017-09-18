import sys

class Solution(object):

    letters=dict({"1":"1",
                  "2":"abc",
                  "3":"def",
                  "4":"ghi",
                  "5":"jkl",
                  "6":"mno",
                  "7":"pqrs",
                  "8":"tuv",
                  "9":"wxyz",
                  "0":"0"})

    def lcr (self,digits,n,output):
        # base case: we've reached the end
        if (n==len(digits)):
            print output
            return
        
        ltrs = self.letters.get(digits[n])
        for i in range (len(ltrs)):
            curr_ltr=ltrs[i]
            output[n]=curr_ltr
            self.lcr(digits,n+1,output)
            
    def letterCombinationsRecursive(self,digits):
        ret=["" for i in range(len(digits))]
        self.lcr(digits,0,ret)
        return ret  
        
    def letterCombinationsIterativeLC(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        # check for bad input              
        for i in range(len(digits)):
            if digits[i] in self.letters:
                pass
            else:
                print "Bad input, expected 0-9 but got a nonvalid digit:",digits
                sys.exit()
        # ret is a list of results so far; initially it is populated with one item,
        # the empty string. Then, for each character in the input string, it looks up
        # the list of letters that match it from the dict defined at the top. It then
        # replaces the list ret with the every combination of existing prefix and possible letter.
        ret = ['']
        for i in range (len(digits)):
            ltrs = self.letters.get(digits[i]) 
            ret = [prefix+letter for prefix in ret for letter in ltrs]
        return ret
        
sol=Solution()

#r=sol.letterCombinationsIterative("23")
#print r

print "IterativeLC"
r=sol.letterCombinationsIterativeLC("234")
print r

print "Recursive"
r=sol.letterCombinationsRecursive("234")
print r
