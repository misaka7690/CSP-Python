data=input().split()
# data=['1', '1', '2', '2', '2', '1', '1', '2', '2', '0']
s=0
start=1
# 记录上次得分
q=0
for d in data:
    d=int(d)
    if d==1:
        s+=1
        q=1
        start=0
    elif d==2:
        if q==1:
            s+=2
            q=2
            start=0
        elif start==1:
            s+=2
            q=2
            start=0
        else:
            q+=2
            s+=q
            start=0
    else:
        break
            
print(s)
