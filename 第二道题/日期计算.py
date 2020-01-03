y=int(input())
d=int(input())

X=30
days=[30]*12
for i in [1,3,5,7,8,10,12]:
    days[i-1]+=1

days[1]=28

if y%400==0:
    days[1]=29
if y%4==0 and y%100:
    days[1]=29

month=0
date=d
while d>0:
    month+=1
    date=d
    d=d-days[month-1]

print(month)
print(date)
