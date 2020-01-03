N=int(input())

data=list(map(int,input().split()))

data.sort()

def Miter(L,f,v):
    L.append(v)
    out=[]
    for i in range(len(L)-1): 
        out.append(f(L[i+1],L[i]))
    return out

q=Miter(data,lambda x,y:y-x,0)
# print(q)
from functools import reduce

ans=reduce(lambda x,y: min(abs(x),abs(y)),q)

print(ans)