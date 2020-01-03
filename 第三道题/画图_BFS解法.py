m,n,q=input().split()

m=int(m)
n=int(n)
q=int(q)

canvas=[['.']*m for _ in range(n)]

def show():
    for i in range(n-1,-1,-1):
        print(''.join(map(str,canvas[i])))


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
# BFS，复杂度为O(4^n)，最后为90分，最后一个算例超时
        x,y,c=d[1:]
        x=int(x)
        y=int(y)

        s=[(x,y)]
        canvas[y][x]=c
        ready=set()
        ready.add((x,y))

        while s:
            tmp=s.pop()

            if tmp[0]+1<m:
                if canvas[tmp[1]][tmp[0]+1] not in ('+','-','|'):
                    if (tmp[0]+1,tmp[1]) not in ready:
                        canvas[tmp[1]][tmp[0]+1]=c
                        ready.add((tmp[0]+1,tmp[1]))
                        s.append((tmp[0]+1,tmp[1]))
            if tmp[0]-1>=0:
                if canvas[tmp[1]][tmp[0]-1] not in ('+','-','|'):
                    if (tmp[0]-1,tmp[1]) not in ready:
                        canvas[tmp[1]][tmp[0]-1]=c
                        ready.add((tmp[0]-1,tmp[1]))
                        s.append((tmp[0]-1,tmp[1]))
            if tmp[1]+1<n:
                if canvas[tmp[1]+1][tmp[0]] not in ('+','-','|'):
                    if (tmp[0],tmp[1]+1) not in ready:
                        canvas[tmp[1]+1][tmp[0]]=c
                        ready.add((tmp[0],tmp[1]+1))
                        s.append((tmp[0],tmp[1]+1))
            if tmp[1]-1>=0:
                if canvas[tmp[1]-1][tmp[0]] not in ('+','-','|'):
                    if (tmp[0],tmp[1]-1) not in ready:
                        canvas[tmp[1]-1][tmp[0]]=c
                        ready.add((tmp[0],tmp[1]-1))
                        s.append((tmp[0],tmp[1]-1))

show()

