n = int(input())
arr = list(map(int, input().split())) 
s=0
d=0
while len(arr)>0:
    l = 0
    r = len(arr) - 1
    chosen=max(arr[l],arr[r])
    s+=chosen
    r-=1
    arr.remove(chosen)
    if len(arr)>0:
        chosen=max(arr[l],arr[r])
        d+=chosen

        r-=1
        arr.remove(chosen)
print(s,d)

    