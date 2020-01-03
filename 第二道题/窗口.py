N,M=input().split()
N=int(N)
M=int(M)

data=[]
for i in range(1,N+1):
    t=list(map(int,input().split()))
    t.append(i)
    data.append(t)

data.reverse()
for i in range(M):
    a,b=input().split()
    a=int(a)
    b=int(b)

    flag=1
    for j,d in enumerate(data):
        if a<=d[2] and a>=d[0] and b>=d[1] and b<=d[3]:
            print(d[4])
            data.pop(j)
            data.insert(0,d)
            flag=0
            break
    
    if flag:
        print('IGNORED')



