n, t = map(int, input().split())
a = list(map(int, input().split()))

left = 0
cur_sum = 0
ans = 0

for right in range(n):
    cur_sum += a[right]

    while cur_sum > t:
        cur_sum -= a[left]
        left += 1

    ans = max(ans, right - left + 1)

print(ans)