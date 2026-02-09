class Solution:    
    def findUnion(self, a, b):
        a= set(a)
        b= set(b)
        # code here
        union=a.union(b)
        return union