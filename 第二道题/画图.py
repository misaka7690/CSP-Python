n=int(input())

chess=[[0]*100 for _ in range(100)]

for _ in range(n):
    a,b,c,d=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)

    for i in range(a,c):
        for j in range(b,d):
            chess[i][j]=1
    
s=sum(map(sum,chess))
print(s)