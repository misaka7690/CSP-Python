# import sys
# sys.stdin=open('input.txt','r')
T, n = input().split()
T = int(T)
n = int(n)

class Data:
    def __init__(self):
        self.data =[]
    # 第i个和第j个进程是否匹配,如果匹配，则消除并返回True，否则返回False
    def f1(self,i,j):
        di=self.data[i]
        dj=self.data[j]

        xi=di[-1]
        xj=dj[-1]

        if xi[0]==xj[0]:
            return False
        
        qi=int(xi[1:])
        qj=int(xj[1:])

        if qi!=j:
            return False
        if qj!=i:
            return False
        
        self.data[i].pop()
        self.data[j].pop()
        return True
    
    # 返回所有发送者和对应的接收者
    def f2(self):
        ans=[]
        for i in range(len(self.data)):
            if self.data[i]:
                x=self.data[i][-1]
                if x[0]=='S':
                    y=int(x[1:])
                    ans.append((i,y))
        return ans
    # 判断data里是否均为[]
    def f3(self):
        for d in self.data:
            if d != []:
                return False
        return True
    # 循环遍历一次,判断是否可以继续执行，是则返回True，否则返回False
    def f4(self):
        t1=self.f2()
        if t1:
            ans=False
            for e in t1:
                i,j=e
                if self.data[j]:
                    if self.f1(i,j):
                        ans=True
                else:
                    return False
            if ans==False:
                return False
            else:
                return True
        else:
            return False
    # 主函数,返回True表示成功执行，否则即失败
    def main(self):
        while self.f3()==False:
            if self.f4()==False:
                return False
        return True

for _ in range(T):
    D=Data()
    for _ in range(n):
        x=input().split()
        x.reverse()
        D.data.append(x)
    tmp=D.main()
    if tmp:
        print(0)
    else:
        print(1)