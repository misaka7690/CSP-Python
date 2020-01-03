a,b,c,y1,y2=map(int,input().split())

# rn 代表闰年
def f1(y):
    if y%400==0:
        return 1
    if y%4==0 and y%100!=0:
        return 1
    return 0

# 返回y年m月第n天是星期几
def f2(y,m,n):
    s=0
    for i in range(1850,y):
        s+=366 if f1(i) else 365
    tmp=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if f1(y):
        tmp[1]=29

    s+=sum(tmp[:m-1])
    s+=n-1
    tmp=[2,3,4,5,6,7,1]
    return tmp[s%7]


# 找回y年a月第b个星期c的日期
def f3(y,a,b,c):
    week = f2(y,a,1)
    tmp1=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    tmp=1
    tmp+=7*(b-1)
    if c>=week:
        tmp+=c-week
    else:
        tmp+=c-week+7
    if f1(y):
        tmp1[1]=29
    if tmp>tmp1[a-1]:
        return None
    else:
        return tmp

for y in range(y1,y2+1):
    t=f3(y,a,b,c)
    if t:
        print('%d/%02d/%02d'%(y,a,t))
    else:
        print('none')