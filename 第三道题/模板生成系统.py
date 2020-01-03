
import re
# import sys
# sys.stdin=open('input.txt','r')
m,n= input().split()
m=int(m)
n=int(n)

text=[]
for _ in range(m):
    text.append(input())

text='\n'.join(text)

names=[]
values=[]

for _ in range(n):
    a,b=input().split(' ',maxsplit=1)
    names.append(a)
    values.append(b.strip('"'))
# 为了满足非递归替换，则需对data排序，让含有{{}}的在最后面
data=list(zip(names,values))
data.sort(key=lambda x: x[1])
names=[ x[0] for x in data]
values=[x[1] for x in data]

for i in range(len(names)):
    name,value=names[i],values[i]
    text=text.replace('{{ '+name+' }}',value)

pat='{{ (.*?) }}'
all=re.findall(pat,text)
for a in all:
    if a not in names:
        text=text.replace('{{ '+a+' }}','')
print(text)


