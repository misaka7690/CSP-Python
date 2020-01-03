data=input().split('-')
# data=['0','670','82162','4']
ans=data[-1]
q=data[0]+data[1]+data[2]
s=0
t=1
for c in q:
    i=int(c)
    s+=i*t
    t+=1
s=s%11
if s==10:
    if ans=='X':
        print('Right')
    else:
        data[-1]='X'
        data='-'.join(data)
        print(data)
else:
    if ans==str(s):
        print('Right')
    else:
        data[-1]=str(s)
        data='-'.join(data)
        print(data)
