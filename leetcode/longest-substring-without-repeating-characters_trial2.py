class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = set()
        max_size = 0
        for right in range(len(s)):
            while left < len(s) and s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])

            max_size = max(max_size, len(window))
        
        return max_size
