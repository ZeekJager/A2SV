class Solution:
    def checkEqual(self, a, b) -> bool:
        sorted_a=sorted(a)
        sorted_b=sorted(b)
        if sorted_a==sorted_b:
            return True
        else:
            return False