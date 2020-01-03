N=int(input())

data=list(map(int,input().split()))

data.sort()

ans=0
for i in range(len(data)-1):
    if data[i+1]==data[i]+1:
        ans+=1

print(ans)
