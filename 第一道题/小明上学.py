r,y,g=map(int,input().split())
N=int(input())

data=[]
for _ in range(N):
    data.append(list(map(int,input().split())))

ans=0
for d in data:
    a,b=d
    if a==0 or a==1:
        ans+=b
    elif a==2:
        ans+=b+r

print(ans)
        