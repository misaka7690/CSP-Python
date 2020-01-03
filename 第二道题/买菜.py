N=int(input())

data1=[]
for _ in range(N):
    data1.append(list(map(int,input().split())))

data2=[]
for _ in range(N):
    data2.append(list(map(int,input().split())))

ans=0
i,j=0,0
while i<len(data1) and j<len(data2):
    a,b=data1[i]
    c,d=data2[j]
    ans+=(lambda x:0 if x<0 else x)( min(b,d)-max(a,c) )
    if b<d:
        i+=1
    else:
        j+=1
print(ans)