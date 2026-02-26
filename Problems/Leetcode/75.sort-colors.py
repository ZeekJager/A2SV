#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(arr)):
            curr=arr[i]
            j=i-1
            while j>=0 and curr<arr[j]:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=curr
# @lc code=end

