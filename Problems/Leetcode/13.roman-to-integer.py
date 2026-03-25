#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000
        s = list(s)
        sum1 = 0

        for i in range(len(s)):
            prev=''
            temp=0
            if s[i] == 'I':
                if s[i+1] == 'V':
                    temp = 4
                elif s[i+1] == 'X':
                    temp = 9
                else:
                    temp=1
            elif s[i] == 'V':
                if s[i-1] == 'I':
                    continue
                temp = 5
            elif s[i] == 'X':
                if s[i-1] == 'I':
                    continue
                elif s[i+1] == 'L':
                    temp = 40
                elif s[i+1] == 'C':
                    temp = 90
                else:
                    temp = 10
            elif s[i] == 'L':
                if s[i-1] == 'X':
                    continue
                temp = 50
            elif s[i] == 'C':
                if s[i-1] == 'X':
                    continue
                elif s[i+1] == 'D':
                    temp = 400
                elif s[i+1] == 'M':
                    temp = 900
                else:
                    temp = 100
            elif s[i] == 'D':
                if s[i-1] == 'C':
                    continue
                else:
                    temp = 500
            elif s[i] == 'M':
                if s[i-1] == 'C':
                    continue
                else:
                    temp = 1000

            sum1 += temp
        print(sum1)
# @lc code=end

