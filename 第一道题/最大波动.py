N=int(input())

data=list(map(int,input().split()))
s=0
for i in range(N-1):
    t=abs(data[i]-data[i+1])
    if t>s:
        s=t

print(s)