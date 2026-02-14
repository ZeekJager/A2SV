t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s=sum(a)
    if s% n!=0:
        print(-1)
        continue
    target=s//n
    k = 0
    for x in a:
        if x > target:
            k += 1
    print(k)