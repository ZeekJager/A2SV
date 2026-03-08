t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    arr=sorted(arr)
    if len(arr)==1 or len(arr)==0:
        print("YES")
    else:
        while len(arr)>1:
            i=0
            if abs(arr[i]-arr[i+1])<=1:
                arr.remove(arr[i])
            else:
                print("NO")
                break
        if len(arr)==1:
            print("YES")