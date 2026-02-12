#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1= sorted(s)
        t1= sorted(t)

        if s1==t1:
            return True
        else:
            return False
        
# @lc code=end

