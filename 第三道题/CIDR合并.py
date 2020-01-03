

n=int(input())

def int2bin(i):
    b=list(bin(i))[2:]
    b=[0]*(8-len(b))+b
    b=list(map(int,b))
    return b

def bin2int(b):
    b='0b'+''.join(map(str,b))
    return int(b,2)

def regular_ip(ip,l):
    bink=[]
    for i in range(4):
        q=int2bin(ip[i])
        for p in q:
            bink.append(p)
    for i in range(l,32):
        bink[i]=0

    ak=[0]*4
    ak[0]=bin2int(list(map(str,bink[:8])))
    ak[1]=bin2int(list(map(str,bink[8:16])))
    ak[2]=bin2int(list(map(str,bink[16:24])))
    ak[3]=bin2int(list(map(str,bink[24:32])))
    return ak



def parser(s):
    ss=s.split('.')
    ls=len(ss)
    ak=[0]*4
    for i in range(ls):
        ak[i]=int(ss[i])
    return ak,ls*8
def a_has_b(a,b):
    pre_a,l_a=a
    pre_b,l_b=b
    if l_a>l_b:
        return False

    tmp1=[pre_a[x]*256**(3-x) for x in range(4)]
    tmp2=[pre_b[x]*256**(3-x) for x in range(4)]

    tmp1=sum(tmp1)//2**(32-l_a)
    tmp2=sum(tmp2)//2**(32-l_b)

    if tmp1==tmp2:
        return True
    else:
        return False

class CIDR:
    def __init__(self):
        self.IPs=[]
    
    def add_data(self,pref,length):
        self.IPs.append([pref,length])
    
    def sort_data(self):
        self.IPs.sort()
    
    def union_data1(self):
        index=0
        while index<len(self.IPs)-1:
            a,b=self.IPs[index],self.IPs[index+1]
            if a_has_b(a,b):
                self.IPs.pop(index+1)
            else:
                index+=1
    
    def union_data2(self):
        index=0
        while index<len(self.IPs)-1:
            a,b=self.IPs[index],self.IPs[index+1]
            if a[1]==b[1]:
                tmp1=[a[0][x]*256**(3-x) for x in range(4)]
                tmp2=[b[0][x]*256**(3-x) for x in range(4)]
                tmp1=sum(tmp1)//2**(32-a[1]+1)
                tmp2=sum(tmp2)//2**(32-b[1]+1)
                if tmp1==tmp2:
                    self.IPs[index][1]-=1
                    self.IPs[index][0]=regular_ip(self.IPs[index][0],self.IPs[index][1])
                    self.IPs.pop(index+1)
                    if index>0:
                        index-=1
                else:
                    index+=1


    def report(self):
        tmp=[]
        for ip in self.IPs:
            pref='.'.join(map(str,ip[0]))
            tmp.append(pref+'/'+str(ip[1]))
        
        for t in tmp:
            print(t)
            
cidr=CIDR()
for _ in range(n):
    s=input().split('/')
    if len(s)==1:
        pref,length=parser(s[0])
        cidr.add_data(pref,length)
    
    if len(s)==2:
        length=int(s[1])
        pref,_=parser(s[0])
        cidr.add_data(pref,length)

cidr.sort_data()
cidr.union_data1()
cidr.union_data2()
cidr.report()

