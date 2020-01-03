n,L,t=input().split()
# n,L,t=3,10,5
n=int(n)
L=int(L)
t=int(t)

data=input().split()
data=list(map(int,data))
index=range(len(data))
temp=zip(data,index)
x=sorted(temp,key=lambda x: x[0])
index=[d[1] for d in x ]
data.sort()
v=[1]*n
# data=[4,6,8]

for _ in range(t):
    for i in range(n):
        # print(v)
        data[i]+=v[i]
    for i,va in enumerate(data):
        if va==L or va==0:
            v[i]*=-1
    for i in range(n-1):
        if data[i]==data[i+1]:
            v[i]*=-1
            v[i+1]*=-1

ans=[0]*n
for i in range(n):
    ans[index[i]]=str(data[i])

ans=' '.join(ans)
print(ans)
