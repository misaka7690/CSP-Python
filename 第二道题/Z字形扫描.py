N=int(input())
data=[]
for _ in range(N):
    data.append(list(map(int,input().split())))

def f(D,F,n):
    ans=[]
    if n<=len(D):
        if F:
            a,b=n-1,0
        else:
            a,b=0,n-1
    else:
        if F:
            a,b=len(D)-1,n-len(D)
        else:
            a,b=n-len(D),len(D)-1
    if n<=len(D):
        for _ in range(n):
            ans.append(D[a][b])
            if F:
                a-=1
                b+=1
            else:
                a+=1
                b-=1
    else:
        for _ in range(2*len(D)-n):
            ans.append(D[a][b])
            if F:
                a-=1
                b+=1
            else:
                a+=1
                b-=1
    return ans

flag=1
q=[]
for i in range(1,2*len(data)):
    q=q+f(data,flag,i)
    if flag:
        flag=0
    else:
        flag=1

print(' '.join(map(str,q)))
