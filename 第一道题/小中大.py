N=int(input())
data=list(map(int,input().split()))
a=data[0]
b=data[-1]
m=N//2
if N-m*2:
    c=data[m]
else:
    c=(data[m-1]+data[m])/2
    if c!=int(c):
        c=round(c,1)
    else:
        c=int(c)
ans=[a,b,c]
ans.sort(reverse=True)
print(' '.join(map(str,ans)))
