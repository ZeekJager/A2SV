#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        count=dict(count)
        res=[]
        for key, value in count.items():
            if value >=2:
                res.append(key)
        
        return res
        
# @lc code=end

