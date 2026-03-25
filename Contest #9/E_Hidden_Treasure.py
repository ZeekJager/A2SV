n, m = map(int, input().split())
L=1
R= n

for _ in range(m):
    parts = input().split()
    direction = parts[2]
    x = int(parts[4])

    if direction == "left":
        R = min(R, x - 1)
    else:
        L = max(L, x + 1)

if L > R:
    print(-1)
else:
    print(R - L + 1)