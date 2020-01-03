import sys
sys.setrecursionlimit(1000000)
m,n,q=input().split()

m=int(m)
n=int(n)
q=int(q)

canvas=[['.']*m for _ in range(n)]
Dx=[1,-1,0,0]
Dy=[0,0,-1,1]

def show():
    for i in range(n-1,-1,-1):
        print(''.join(map(str,canvas[i])))

def DFS(x,y,c):
    canvas[y][x]=c
    for dx,dy in zip(Dx,Dy):
        xx,yy=x+dx,y+dy
        if 0<=xx<m and 0<=yy<n and canvas[yy][xx] not in ('+','-','|',c):
            DFS(xx,yy,c)
            

for _ in range(q):
    d=input().split()
    t=int(d[0])

    if t==0:
        x1,y1,x2,y2=list(map(int,d[1:]))
        if x1==x2:
            y1,y2=[y1,y2] if y1<y2 else [y2,y1]
            for i in range(y1,y2+1):
                if canvas[i][x1] in ('-','+'):
                    canvas[i][x1]='+'
                else:
                    canvas[i][x1]='|'
        if y1==y2:
            x1,x2=[x1,x2] if x1<x2 else [x2,x1]
            for i in range(x1,x2+1):
                if canvas[y1][i] in ('|','+'):
                    canvas[y1][i]='+'
                else:
                    canvas[y1][i]='-'

    if t==1:
# DFS减小时间复杂度,也是90分，最后一个算例为运行错误，猜测为递归错误，但似乎并不是这个原因。
        x,y,c=d[1:]
        x=int(x)
        y=int(y)

        DFS(x,y,c)

show()

