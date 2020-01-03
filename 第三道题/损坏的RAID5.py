n,s,l=map(int,input().split())

class Blk:
    def __init__(self):
        self.data =None
        self.index =None
        self.p=False

class Dsk:
    def __init__(self,k):
        self.blks = [Blk() for _ in range(k)]
    
    def set_P(self,a,s):
        for i in range((a-1)*s,a*s):
            self.blks[i].p=True
    
    def set_index(self,a,s,h):
        

class RAID5:
    def __init__(self,n,s):
        self.n = n
        self.s = s
        self.k = 0
        self.first = True

    def next(self,i):
        i-=1
        if i==-1:
            return self.n-1
        return i
    def set_P(self):
        self.raid5=[Dsk(self.k) for i in range(self.n)]
        last=self.n-1
        for i in range(self.k//self.s):
            self.raid5[last].set_P(i,self.s)
            last=self.next(last)
        


    
    
    def readdata(self,data):
        data=data.split()
        x=int(data[0])
        data=data[1]
        if self.first:
            self.first=False
            l=len(data)
            self.k=l//8
            self.set_P()

        
        self.raid5[x]=data
        
            

        


    

    


    

    


