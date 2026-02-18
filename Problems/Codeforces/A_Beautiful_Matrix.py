matrix=[[],[],[],[],[]]
for i in range(5):
    r= list(map(int, input().rstrip().split()))
    matrix[i]=r

loc_1=[]
for i in range(5):
    for j in range(5):
        if matrix[i][j]==1:
            loc_1=[i,j]

x=2
y=2

answer=(abs(loc_1[0]-x) + abs(loc_1[1]-y))
print(answer)