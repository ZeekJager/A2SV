#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        n=len(num)
        l=0
        r=n-1

        while l<r:
            c=num[l]+num[r]
            if c == target:
                return[l+1,r+1]
            elif c > target:
                r-=1
            elif c < target:
                l+=1
            
# @lc code=end

