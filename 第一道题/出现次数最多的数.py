N=int(input())

data=list(map(int,input().split()))

from collections import Counter

data=Counter(data)
data=data.most_common(1)
print(data)
q=data[0][1]
ans=[]
for a,b in data:
    if b==q:
        ans.append(a)

print(min(ans))
