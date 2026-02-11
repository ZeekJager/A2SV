#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        max=0
        
        for x in count:
            if max<count.get(x):
                max=count.get(x)
                num=x
        return num
            

        # Counter({2: 4, 1: 3})
# @lc code=end

