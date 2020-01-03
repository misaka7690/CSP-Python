n,m=input().split()
n=int(n)
m=int(m)

data=[]
for _ in range(n):
    data.append(input().split())

for i in range(m-1,-1,-1):
    q=[]
    for j in range(n):
        q.append(data[j][i])
    print(' '.join(q))
