N=int(input())

data=list(map(int,input().split()))

S=set(data)
D={}
for s in S:
    D[s]=0

ans=[]
for d in data:
    D[d]+=1
    ans.append(D[d])

ans=map(str,ans)
print(' '.join(ans))