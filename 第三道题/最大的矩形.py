# 这个是40分，因为运行超时,复杂度为O(n^3)
#-------------------------------------------------
# n=int(input())

# data=list(map(int,input().split()))

# D=[[0]*n for _ in range(n)]

# for i in range(n):
#     for j in range(i+1,n):
#         D[i][j]=min(data[i:j+1])*(j+1-i)

# print(max(map(max,D)))
#-------------------------------------------------

# 利用动态规划减小复杂度,为O(n^2),最终得100分
n=int(input())

data=list(map(int,input().split()))
D=[]
def f(i):
    m=100000
    t=0
    for j in range(i,n):
        m=min(m,data[j])
        t=max(t,m*(j+1-i))
    return t

ans=0
for i in range(n):
    ans=max(ans,f(i))
print(ans)