#
# @lc app=leetcode id=789 lang=python3
#
# [789] Escape The Ghosts
#

# @lc code=start
import math
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dg=[]
        dp=abs(target[0]) +abs(target[1])
        for i in range(len(ghosts)):
            dg.append((abs(target[1]-ghosts[i][1]))+ (abs(target[0]-ghosts[i][0])))
        m=min(dg)
        if dp< m:
            return True
        else:
            return False
# @lc code=end

