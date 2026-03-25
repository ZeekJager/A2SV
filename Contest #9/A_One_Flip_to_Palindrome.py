t = int(input())
ans = []

for _ in range(t):
    n = int(input())
    s = input().strip()

    m = n // 2
    first = -1
    last = -1

    for i in range(m):
        if s[i] != s[n - 1 - i]:
            if first == -1:
                first = i
            last = i

    ok = True
    if first != -1:
        for i in range(first, last + 1):
            if s[i] == s[n - 1 - i]:
                ok = False
                break

    ans.append("Yes" if ok else "No")

print("\n".join(ans))