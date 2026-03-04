n,m= map(int, input().split())
arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
t=0
b=0
c=0
# output=[]
# while b<m:
#     if t>=n:
#         output.append(c)
#         b += 1
#     else:
#         if arr1[t]<arr2[b]:
#             c+=1
#             t+=1
#         else:
#             output.append(c)
#             b+=1
# print(" ".join(map(str,output)))
output=[]
first = 0
for second in range(m):
	while first < n and arr1[first]<arr2[second]:
		first += 1
	output.append(first)
print(" ".join(map(str,output)))