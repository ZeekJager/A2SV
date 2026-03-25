#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=(''.join(ch for ch in s if ch.isalnum())).lower
        n=len(s)
        i=0
        j=n-1
        while i<j:
            if s[i]== s[j]:
                i+=1
                j-=1
            else:
                return False
        return True
# @lc code=end

