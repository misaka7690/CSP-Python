n=int(input())
m=int(input())

classmate=list(range(1,n+1))

def Myfind(L,x):
    for i,e in enumerate(L):
        if e==x:
            return i
for _ in range(m):
    p,q=input().split()
    p=int(p)
    q=int(q)

    i=Myfind(classmate,p)
    classmate.pop(i)
    classmate.insert(i+q,p)

print(' '.join(map(str,classmate)))

