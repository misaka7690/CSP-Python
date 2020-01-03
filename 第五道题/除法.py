# import sys
# sys.stdin=open('input.txt','r')
from  itertools import accumulate
N,M=input().split()
N=int(N)
M=int(M)

class DataSet:
    def __init__(self):
        self.data = []
        self.sum = []
        self.delta=[0]*10**5
    
    def sum_init(self):
        self.sum=[0]+list(accumulate(self.data))

    def opt1(self,l,r,v):
        if v==1:
            return
        l-=1
        r-=1
        for i in range(l,r+1):
            q=self.data[i]%v
            if q==0:
                self.data[i]=self.data[i]//v
                self.delta[i]-=self.data[i]*(v-1)
    
    def opt2(self,l,r):
        t=self.sum[r]-self.sum[l-1]
        q=sum(self.delta[l-1:r])
        print(t+q)

dataset = DataSet()
dataset.data = list(map(int,input().split()))
dataset.sum_init()
for _ in range(M):
    opt=list(map(int,input().split()))
    if opt[0]==1:
        dataset.opt1(opt[1],opt[2],opt[3])
    else:
        dataset.opt2(opt[1],opt[2])