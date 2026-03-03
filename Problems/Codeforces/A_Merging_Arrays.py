n, m = map(int, input().split())
arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))

l=0
r=0
output=[]
while l<n and r<m:
    if arr1[l]<arr2[r]:
        output.append(arr1[l])
        l+=1
    else:
        output.append(arr2[r])
        r+=1
output.extend(arr1[l:])
output.extend(arr2[r:])
print(" ". join(map(str, output)))
    