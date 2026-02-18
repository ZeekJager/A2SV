#
# @lc app=leetcode id=3160 lang=python3
#
# [3160] Find the Number of Distinct Colors Among the Balls
#

# @lc code=start
from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res=[]
        ballmap={}
        c= defaultdict(list)
        for ball, color in queries:
            if ball in ballmap:
                c[ballmap[ball]].remove(ball)
                if not c[ballmap[ball]]:
                    del c[ballmap[ball]]
            ballmap[ball]=color
            c[color].append(ball)
            res.append(len(c))
        return res
            

                    
# @lc code=end

