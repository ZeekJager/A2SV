#
# @lc app=leetcode id=1893 lang=python3
#
# [1893] Check if All the Integers in a Range Are Covered
#

# @lc code=start
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left,right+1):
            covered=False
            for r in ranges:
                if r[0]<=i<=r[1]:
                    covered=True
                    break
            if not covered:
                return False
        return True
# @lc code=end

