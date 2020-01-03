N=int(input())//10

ans=0
while N>0:
    if N>=5:
        N-=5
        ans+=7
    elif N>=3:
        N-=3
        ans+=4
    else:
        ans+=N
        break



print(ans)
