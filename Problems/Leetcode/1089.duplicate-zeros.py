#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#

# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr.sorted()
        n=len(arr)
        c=arr.count(0)
        i=n-1
        j=n+c-1
        while i<j:
            if j<n:
                arr[j]=arr[i]
            if arr[i]==0:
                j-=1
                if j<n:
                    arr[j]=0
            i-=1
            j-=1

            

# @lc code=end

