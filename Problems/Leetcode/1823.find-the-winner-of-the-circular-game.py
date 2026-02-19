#
# @lc app=leetcode id=1823 lang=python3
#
# [1823] Find the Winner of the Circular Game
#

# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        p=0
        a=[]
        for i in range(1,n+1):
            a.append(i)
        while len(a)>=2:
            p=(p+k-1)%len(a)
            a.remove(a[p])
            
        return a[0]

# @lc code=end

