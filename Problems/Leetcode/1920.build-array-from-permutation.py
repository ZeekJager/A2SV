#
# @lc app=leetcode id=1920 lang=python3
#
# [1920] Build Array from Permutation
#

# @lc code=start
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        new_list=[]
        for i in range(len(nums)):
            new_list.append(nums[nums[i]])

        return new_list
        
# @lc code=end

