t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int,input().split())))

    if n == 1 and m == 1:
        print(-1)
    else:
        for i in range(1,n):
            for j in range(1,m):
                print(matrix[i][j],end = " ")
            print(matrix[i][0])
        for i in range(1):
            for j in range(1,m):
                print(matrix[i][j],end = " ")
            print(matrix[i][0])
