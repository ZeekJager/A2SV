t = int(input())
for _ in range(t):
    n=int(input())
    if n%2==0 and n!=2:
        print (0)
    elif n%2!=0 and n!=2:
        print(1)
    else:
        print(2)
