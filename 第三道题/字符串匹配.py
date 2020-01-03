import re

s=input()
flag=int(input())
n=int(input())

obj=[]
for _ in range(n):
    obj.append(input())



pat=s
if flag==0:
    flags=re.I
else:
    flags=0

ans=[]
for o in obj:
    t=re.search(pat,o,flags=flags)
    if t is not None:
        ans.append(o)
    
ans='\n'.join(ans)
print(ans)