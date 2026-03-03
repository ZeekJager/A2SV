t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    n = len(arr)

    ans = float('inf')
    for i in range(n - 2):
        a, b, c = arr[i], arr[i+1], arr[i+2]
        median = b 
        cost = abs(a - median) + abs(b - median) + abs(c - median)
        ans = min(ans, cost)
    print(ans)
