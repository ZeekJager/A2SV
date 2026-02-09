#User function Template for python3

# class Solution:
#     #Function to check if a is a subset of b.
#     def isSubset(self, a, b):
a= [11, 7, 1, 13, 21, 3, 7, 3]
b= [11,3, 7, 1, 7]
a=sorted(a)
print(a)
b=sorted(b)
print (b)

new_a=[]

for i in range(len(b)):
    new_a.append(a[i])

print (new_a==b)


    
    
