N=int(input())

data=list(map(int,input().split()))

ans=0
for i in range(1,len(data)-1):
    if data[i]>data[i+1] and data[i]>data[i-1]:
        ans+=1
    if data[i]<data[i+1] and data[i]<data[i-1]:
        ans+=1

print(ans)