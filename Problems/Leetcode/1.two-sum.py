#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i, n in enumerate(nums):
            t= target-n
            if t in dict1:
                return [dict1[t],i]
            dict1[n]=i
# @lc code=end


