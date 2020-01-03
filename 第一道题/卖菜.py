N=int(input())
data=list(map(int,input().split()))

ans=[0]*N
for i in range(N):
    if i==0:
        ans[i]=(data[i]+data[i+1])//2
    elif i==N-1:
        ans[i]=(data[i-1]+data[i])//2
    else:
        ans[i]=(data[i-1]+data[i]+data[i+1])//3

print(' '.join(map(str,ans)))