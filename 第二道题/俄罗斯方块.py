D=[]
for _ in range(15):
    D.append(list(map(int,input().split())))

D.append([0]*10)
D.append([0]*10)
D.append([0]*10)
D.append([0]*10)


E=[]
for _ in range(4):
    E.append(list(map(int,input().split())))

indent=int(input())
q=0
p=4
for i in range(4):
    if E[:][i]==[0]*4:
        q+=1
    else:
        break
for i in range(3,0,-1):
    if E[i][:]==[0]*4:
        p-=1
    else:
        break

G=[[0]*(4-q) for _ in range(p)]
for i in range(q,4):
    for j in range(p):
        G[j][i-q]=E[j][i]

a=p
b=4-q

flag=1

def check(x,y):
    print(x,y)
    for i in range(x,x+a):
        for j in range(y,y+b):
            print(i,j)
            if D[i][j]!=G[i-x][j-y]:
                return 0
        return 1
x=indent-q
y=0
while check(x,y):
    y+=1
