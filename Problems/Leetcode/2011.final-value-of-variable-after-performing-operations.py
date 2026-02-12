#
# @lc app=leetcode id=2011 lang=python3
#
# [2011] Final Value of Variable After Performing Operations
#

# @lc code=start
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for i in range(len(operations)):
            if operations[i] =="++X" or operations[i] =="X++":
                x+=1
            else:
                x-=1
        return x
# @lc code=end

