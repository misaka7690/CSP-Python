N=int(input())

data=list(map(int,input().split()))

ans=0
for d in data:
    if -d in data:
        ans+=1
    
print(ans//2)

