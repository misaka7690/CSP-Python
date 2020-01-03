# import sys
# sys.stdin=open('input.txt','r')
n,m=input().split()
n=int(n)
m=int(m)
json=''
for i in range(n):
    json+=input()

json=eval(json)

exp=[]
for i in range(m):
    exp.append(input())

for i in range(m):
    if exp[i] in json :
        if type(json[exp[i]]) is dict:

            print('OBJECT')
        else:
            print('STRING '+json[exp[i]])
    else:
        eps=exp[i].split('.')
        l=len(eps)
        if l==1:
            print('NOTEXIST')
        else:
            d=json
            flag=1
            for j in range(l):
                if eps[j] in d:
                    d=d[eps[j]]
                else:
                    print('NOTEXIST')
                    flag=0
                    break
            if flag:
                if type(d) is dict:
                    print('OBJECT')
                else:
                    print('STRING '+d)

# print('finished')