#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start
from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        output=[]
        count=Counter(arr1)
        for i in arr2:
            for j in range(count[i]):
                output.append(i)
            del count [i]
        s=dict(sorted(count.items()))
        for key in s:
            for j in range(s[key]):
                output.append(key)

        return output
# @lc code=end

