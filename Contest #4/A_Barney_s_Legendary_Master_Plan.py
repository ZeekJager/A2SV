t = int(input())
for _ in range(t):
    n = int(input())
    target = list(map(int, input().split()))
    unique=len(set(target))
    if unique == 1:
        print(1)
    else:
        print(2*unique -1)




