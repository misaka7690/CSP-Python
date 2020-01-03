N,K=input().split()
N=int(N)
K=int(K)

data=[]
for _ in range(K):
    w,s,c=map(int,input().split())
    data.append((s,1,w))
    data.append((s+c,0,w))

def Myfind(L,x):
    for i,e in enumerate(L):
        if e==x:
            return i

data.sort()
KEY=list(range(1,N+1))
X=-1
for s,f,w in data:
    if f==1:
        i=Myfind(KEY,w)
        KEY[i]=X
    else:
        for i,c in enumerate(KEY):
            if c==X:
                KEY[i]=w
                break

print(' '.join(map(str,KEY)))





