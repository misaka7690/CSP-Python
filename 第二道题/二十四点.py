# N=int(input())

# for i in range(N):
#     if eval(input().replace('x','*').replace('/','//'))==24:
#         print('Yes')
#     else:
#         print('No')

# 法二，正规做法
N=int(input())

def f(formula):
    formula=list(formula)
    temp=[]
    for i,c in enumerate(formula):
        try:
            c=int(c)
            temp.append(c)
        except ValueError:
            if c=='+' or c=='-':
                temp.append(c)
            else:
                a=temp.pop()
                b=int(formula.pop(i+1))
                if c=='x':
                    temp.append(a*b)
                else:
                    temp.append(a//b)
    ans=temp[0]
    for i in range(1,len(temp),2):
        # print(i)
        if temp[i]=='+':
            ans+=temp[i+1]
        else:
            ans-=temp[i+1]
        # print(ans)
    if ans==24:
        return 'Yes'
    else:
        return 'No'

# f('1x9-5/9')
# f('1x1+9-9')
# f('6x4+4/5')
for i in range(N):
    print(f(input()))
