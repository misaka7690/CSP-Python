S=input().split()
n=int(S[0])
k=int(S[1])

L=list(range(1,n+1))
tot=0
pos=0
while len(L)>1:
    tot+=1
    if pos==len(L):
        pos=0
    if tot%k==0 or tot%10==k:
        # print(L.pop(pos))
        L.pop(pos)
    else:
        pos+=1

print(L[0])