t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    arr = [0] * k
    for _ in range(k):
        a,b = map(int,input().split())
        arr[a-1] += b
    arr.sort(reverse=True)

    print(sum(arr[:n]))
