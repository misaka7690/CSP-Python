import sys
sys.stdin=open('input.txt','r')
n,m=map(int,input().split())

class Node:
    def __init__(self):
        self.id=None
        self.flag=None
        self.order=None
        self.index=None

    def readdata(self,data):
        self.order=data.count('.')//2
        data=data.strip('.').split()
        self.flag=data[0].lower()
        if len(data)==2:
            self.id=data[1]
    def setindex(self,index):
        self.index=index
    def data_equal(self,data):
        if data==self.flag or data==self.id:
            return True
        return False
class Document:
    def __init__(self):
        self.doc = []
    
    def addnode(self,node):
        self.doc.append(node)
    
    def findid(self,data):
        ans=[]
        for i,node in enumerate(self.doc):
            if node.id == data:
                ans.append(i+1)
        if ans==[]:
            return [0]
        return [len(ans)]+ans

    def findflag(self,data):
        ans=[]
        for i,node in enumerate(self.doc):
            if node.flag == data:
                ans.append(i+1)
        if ans==[]:
            return [0]
        return [len(ans)]+ans

    def select_one(self,sel):
        if sel.id:
            return self.findid(sel.data)
        else:
            return self.findflag(sel.data)
    
    def has_father(self,i,father):
        tmp=self.father(i)
        if tmp:
            return tmp.data_equal(father)
        return None
    
    def has_fathers(self,t,fathers):
        if len(fathers)==1:
            father=fathers[0]
            return self.has_father(t,father)
        
        next=self.father(t)
        if next and next.data_equal(fathers[-1]):
            fathers.pop()
            return self.has_fathers(next.index,fathers)
        return False



    def select_all(self,sel):
        last=sel.data[-1]
        fathers=sel.data[0:-1]
        if last[0]=='#':
            tmp=self.findid(last)
        else:
            tmp=self.findflag(last)
        
        if len(tmp)==1:
            return tmp
        ans=[]
        tmp=tmp[1:]
        for t in tmp:
            if self.has_fathers(t,fathers):
                ans.append(t)
        return [len(ans)]+ans


    def select(self,sel):
        if sel.one:
            return self.select_one(sel)
        else:
            return self.select_all(sel)
    def father(self,index):
        node = self.doc[index-1]
        i=index
        tmp=self.doc[i-1]
        while tmp.order >= node.order and i!=-1:
            i-=1
            tmp=self.doc[i-1]
        if i==-1:
            return None
        else:
            return tmp

class Selector:
    def __init__(self):
        self.data=None
        self.id=False
        self.flag=False
        self.one=True
    def readdata(self,data):
        data=data.split()
        if len(data)==1:
            self.data=data[0]
            data=data[0]
            if data[0]=='#':
                self.id=True
            else:
                self.flag=True
                self.data=self.data.lower()
        else:
            for i in range(len(data)):
                if data[i][0]!='#':
                    data[i]=data[i].lower()
            self.data=data
            self.one=False


document=Document()
for i in range(n):
    node=Node()
    x=input()
    node.readdata(x)
    node.setindex(i+1)
    document.addnode(node)

for _ in range(m):
    sel=Selector()
    x=input()
    sel.readdata(x)
    ans=document.select(sel)
    print(' '.join(map(str,ans)))

