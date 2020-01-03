n,m=input().split()
n=int(n)
m=int(m)

data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))

flags=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m-2):
        if data[i][j]==data[i][j+1]==data[i][j+2]:
            flags[i][j]=flags[i][j+1]=flags[i][j+2]=1
for j in range(m):
    for i in range(n-2):
        if data[i][j]==data[i+1][j]==data[i+2][j]:
            flags[i][j]=flags[i+1][j]=flags[i+2][j]=1

for i in range(n):
    for j in range(m):
        if flags[i][j]==1:
            data[i][j]=0

for i in range(n):
    print(' '.join(map(str,data[i])))