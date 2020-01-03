nk=input().split()
n=int(nk[0])
k=int(nk[1])

data=list(map(int,input().split()))

ans=0
s=0
while data:
    s+=data.pop()
    if s>=k:
        ans+=1
        s=0
if s:
    ans+=1
print(ans)
