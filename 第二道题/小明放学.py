r,y,g=map(int,input().split())
N=int(input())

data=[]
for _ in range(N):
    data.append(list(map(int,input().split())))


def f(a,b,t):
    t=t%(r+y+g)
    if a==0:
        return a,b
    if t<b:
        return a,b-t
    #红灯1，后面是绿灯3,再是黄灯2
    if a==1:
        return f(3,g,t-b)
    elif a==2:
        return f(1,r,t-b)
    elif a==3:
        return f(2,y,t-b)
    else:
        return a,b

ans=0 
for d in data:
    a,b=f(d[0],d[1],ans)
    if a==0 or a==1:
        ans+=b
    elif a==2:
        ans+=b+r
print(ans)
