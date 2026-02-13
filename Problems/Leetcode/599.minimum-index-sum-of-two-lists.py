#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res=[]
        index_sum=sys.maxsize
        dict1 = {value: i for i, value in enumerate(list1)}
        for i, name in enumerate(list2
        ):
            if list2[i] in dict1:
                total=dict1[name] +i
                if total < index_sum:
                    index_sum=total
                    res=[name]
                elif total ==index_sum:
                    res.append(name)
        
        return res
        
# @lc code=end

