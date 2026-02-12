#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result=[]
        word_lists = [list(w) for w in words]

        for ch in word_lists[0]:
            temp=True
            for s in word_lists[1:]:
                if ch in s:
                    temp= (temp and True)
                    s.remove(ch)
                else:
                    temp=False
                    break
            if temp==True:
                result.append(ch)

        return result
        
# @lc code=end

