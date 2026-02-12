t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    largest=max(arr)
    arr.remove(largest)
    if arr[0] + arr[1] == largest:
        print("YES")
    else:
        print("NO")
    