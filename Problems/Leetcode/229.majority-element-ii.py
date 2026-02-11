#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (55.65%)
# Likes:    10913
# Dislikes: 493
# Total Accepted:    1.2M
# Total Submissions: 2.2M
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,2,3]
# Output: [3]
# 
# 
# Example 2:
# 
# 
# Input: nums = [1]
# Output: [1]
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2]
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
# 
# 
# 
# Follow up: Could you solve the problem in linear time and in O(1) space?
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count=Counter(nums)
        max=[]
        n=len(nums)
        
        for x in count:
            if count.get(x) > (n//3):
                max.append(x)
        return max
        
# @lc code=end

