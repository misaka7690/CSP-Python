# 如果开盘价为p0，则系统可以将所有出价至少为p0的买单和所有出价至多为p0的卖单进行匹配。
# 因此，此时的开盘成交量为出价至少为p0的买单的总股数和所有出价至多为p0的卖单的总股数之间的较小值。
import sys
sys.stdin=open('input.txt','r')

class ETF:
    def __init__(self):
        self.sells=[]
        self.buys=[]
    
    def readdata(self):
        all=sys.stdin.read().split('\n')
        # 全部内部split
        tmp=[]
        # 记录取消记录的序号
        tmp1=[]
        for a in all:
            x=a.split()
            tmp.append(x)
            if len(x)==2:
                tmp1.append(int(x[1]))
        for i in range(len(tmp)):
            if i+1 not in tmp1 and len(tmp[i])>2:
                if tmp[i][0][0]=='s':
                    self.sells.append(tmp[i][1:])
                else:
                    self.buys.append(tmp[i][1:])
        for i in range(len(self.sells)):
            self.sells[i]= list(map(float,self.sells[i]))
        
        for i in range(len(self.buys)):
            self.buys[i]= list(map(float,self.buys[i]))
    
        
    def print(self):
        print(self.sells)
        print(self.buys)


etf=ETF()
etf.readdata()
etf.print()
    
                 
