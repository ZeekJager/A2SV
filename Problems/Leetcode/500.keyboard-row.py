#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result=[]
        r1 = set(['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'q','w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        r1=set(r1)
        r2 = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        r2=set(r2)
        r3= ['Z', 'X', 'C', 'V', 'B', 'N', 'M', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
        r3=set(r3)

        for word in words:
                l=set(word)
                if l.issubset(r1) or l.issubset(r2) or l.issubset(r3):
                        result.append(word)
        return result
                
# @lc code=end

