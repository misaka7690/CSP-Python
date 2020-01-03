N=int(input())

data=list(map(int,input().split()))

ans=1
for i in range(N-1):
    if data[i]!=data[i+1]:
        ans+=1
print(ans)
    