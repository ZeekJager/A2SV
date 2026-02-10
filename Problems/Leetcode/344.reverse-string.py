#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j=len(s)-1
        for i in range(len(s)):
            
            if j<=i:
                break
            else:
                s[i], s[j] = s[j], s[i]
                j-=1
# @lc code=end

