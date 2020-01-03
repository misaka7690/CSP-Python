N=int(input())

data=list(map(int,input().split()))

S=set(data)

flag=1
for s in S:
    pos=0
    neg=0
    for d in data:
        if s>d:
            pos+=1
        if s<d:
            neg+=1
    if pos==neg:
        print(s)
        flag=0
        break

if flag:
    print(-1)