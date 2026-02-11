#
# @lc app=leetcode id=1790 lang=python3
#
# [1790] Check if One String Swap Can Make Strings Equal
#

# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1=list(s1)
        s2=list(s2)
        diff=[]
        s_s1=sorted(s1)
        s_s2=sorted(s2)
        if s1==s2:
            return True
        if s_s1 != s_s2:
            return False
        print(s_s1)
        for i in range(len(s1)):
            if s1[i]==s2[i]:
                continue
            else:
                diff.append(i)
        if len(diff)>2:
            return False
        else:
            return True
            
        
# @lc code=end

