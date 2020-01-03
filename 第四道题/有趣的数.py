import itertools
from math import factorial
n=int(input())
M=1000000007

# 求组合数大小
def f1(n,k):
    up=factorial(n)
    down=factorial(k)*factorial(n-k)
    return up//down


# 返回n=a+b+c+d的拆分结果，直接给a+b的dict即可
def f2(n):
    ans={}
    for i in range(2,n-1):
        ans[i] =f1(i-1,1)*f1(n-i-1,1)
    return ans

# 确定a+b的值对应的分配总数
def f3(n,ab):
    return f1(n-1,ab)

ans =0
tmp=f2(n)
for k,v in tmp.items():
    ans+=v*f3(n,k)

print(ans%M)