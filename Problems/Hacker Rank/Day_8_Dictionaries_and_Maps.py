import sys
dict1={}
test=int(input())
for i in range(test):
    name,number=input().split()

    dict1[name]=number

for line in sys.stdin:
    q=line.strip()

    if q in dict1:
        print(q+'=' + dict1[q])
    else:
        print("Not found")
