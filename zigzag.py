import numpy as np

class Solution(object):
 
    
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        done=False
        m=[[""] for i in range(numRows)]
        i=0
        print "s=",s," r=",numRows
        if (numRows == 1):
            return s
        while(not done):
            for r in range (numRows-1):
                # down
                if (i<len(s)):
                    m[r].append(s[i])
                    #print "adding1 ",s[i], " at r=",r, " i=",i
                    i+=1
            for r in range (numRows-1,0,-1):
                # diagonally up
                if (i<len(s)):
                    m[r].append(s[i])
                    #print "adding2 ",s[i], " at r=",r
                    i+=1
                    
            if (i==len(s)):
                done=True

        ret=""
        for r in range (numRows):
            ret = ret + "".join([str(i) for i in m[r]])
        return ret

                
sol=Solution()
s=sol.convert("PAYPALISHIRING",3)
print s

s=sol.convert("A",1)
print s

s=sol.convert("AB",1)
print s

s=sol.convert("ABC",2)
print s


#s=sol.convert("obanbumdladpycygtrgutpdzlajzovccwcqaycfjeibclzkgsqanifmtfxsusuyqzoqxsyjwgkatllbfdesljggpdalxvjnwygvqegpmspgdcjignctxiaonazkxiyvigrbkzqwsfexiogodkjatlqioptlatjkzcllbbhthorpezfhjqkecapqsidubmecoqnsrulakerofyyrpivrkkheumyxzdzpvmhmjvpvbgkhfkyusvneiwjcijajmbzjqiwzfnuhtgoaqmukhjrpfauojwzyxyhnjfooslxorlokzlwjunaanuqzqpzqqifzoupifnwyankayhjsujukgklyckqsswtiskrzxpzackccrlxnwrxecifeuvynrrxlbqkbgkdkufpnsmaqdavhkanfxluperciinlqxoctvrindifjkaqvcgaaruryntivitnhjqcghktnvywfbocfuchoyammwwjerxoapqiwbblwbjdeygksktijuwxqsiwjhklwbtvcwgaaqfeqlqkykthgpgwkostwfhsgapkzw",317)
print s

#s=sol.convert("ciyspxxqcvibfdeensgjgpzqcmnoxwoagouylroppyquevarnictyemaqzoqxesesmcffsxurnqvkqozztvxxhzpiphguzkonowt",71)
print s
