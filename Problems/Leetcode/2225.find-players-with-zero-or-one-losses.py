#
# @lc app=leetcode id=2225 lang=python3
#
# [2225] Find Players With Zero or One Losses
#

# @lc code=start
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses={}
        
        answer=[]
        for winner,loser in matches:
            losses[loser]=losses.get(loser,0)+1
            losses[winner]= losses.get(winner,0)
        # for i in range(len(matches)):
        #     losses[matches[i][1]]=losses.get(matches[i][1],0)+ 1
        #     losses[matches[i][0]]= losses.get(matches[i][0],0)
        no_loss=[key for key, value in losses.items() if value == 0]
        no_loss.sort()
        one_loss=[key for key, value in losses.items() if value == 1]
        one_loss.sort()
        answer = [no_loss,one_loss]
        
        return answer
        
# @lc code=end

