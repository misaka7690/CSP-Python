n=int(input())
data=list(map(int,input().split()))

D=[[x,x+1,x+2,x+3,x+4] for x in range(1,100,5) ]

X=-1
def f(L,r):
    q=0
    while q+r<=5:
        flag=1
        for j in range(q,q+r):
            if L[j]==X:
                flag=0
                break
        if flag:
            return q
        else:
            q+=1
    return None

ans=[]    
for d in data:
    another_flag=1
    for i,e in enumerate(D):
        if f(e,d) is not None:
            t=[]
            for j in range(f(e,d),f(e,d)+d):
                t.append(D[i][j])
                D[i][j]=X
            ans.append(t)
            another_flag=0
            break
    if another_flag:
        t=[]
        for i in range(20):
            for j in range(5):
                if D[i][j]!=X and d:
                    t.append(D[i][j])
                    D[i][j]=X
                    d-=1
        ans.append(t)

for i in range(len(ans)):
    print(' '.join(map(str,ans[i])))