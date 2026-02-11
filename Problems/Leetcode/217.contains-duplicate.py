#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count= Counter(nums)
        count=dict(count)
        for i in count:
            if count.get(i)>=2:
                return True
        return False
        
# @lc code=end

