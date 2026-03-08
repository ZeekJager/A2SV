t = int(input())  

for _ in range(t):
    n = int(input())  
    a = list(map(int, input().split())) 
  
    a.sort()

    c_s = a[0]
    e_s = a[-1]

    crowd_count = 1
    elite_count = 1

    i = 1
    j = n - 2

    possible = False

    while i <= j:
        if e_s > c_s and elite_count < crowd_count:
            possible = True
            break

        c_s += a[i]
        crowd_count += 1
        i += 1

        if e_s > c_s and elite_count < crowd_count:
            possible = True
            break

        e_s += a[j]
        elite_count += 1
        j -= 1

    if e_s > c_s and elite_count < crowd_count:
        possible = True

    print("YES" if possible else "NO")