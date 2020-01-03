T=int(input())

q0,q1,q2,q3,q4,q5,q6=0.03,0.1,0.2,0.25,0.3,0.35,0.45
def Myf(s):
    if s<3500:
        return s
    A=s-3500
    if A<1500:
        return s-A*q0
    A=A-1500
    if A<3000:
        return s-1500*q0-A*q1
    A=A-3000
    if A<4500:
        return s-1500*q0-3000*q1-A*q2
    A=A-4500
    if A<26000:
        return s-1500*q0-3000*q1-4500*q2-A*q3
    A=A-26000
    if A<20000:
        return s-1500*q0-3000*q1-4500*q2-26000*q3-A*q4
    A=A-20000
    if A<25000:
        return s-1500*q0-3000*q1-4500*q2-26000*q3-20000*q4-A*q5
    A=A-25000
    return s-1500*q0-3000*q1-4500*q2-26000*q3-20000*q4-25000*q5-A*q6

start=(T//100)*100
t=start
while True:
    if Myf(t)==T:
        print(t)
        break
    else:
        t+=100


