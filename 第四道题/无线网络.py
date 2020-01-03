n,m,k,r=map(int,input().split())

Black=1
# 已访问
Red=2
# 未访问
White=3
class Point:
    def __init__(self):
        self.x = None
        self.y = None
        self.color=White
    def Indistance(self, other):
        global r
        t=(self.x-other.x)**2 + (self.y-other.y)**2
        if t<=r**2:
            return True
        else:
            return False

NBOX=[]
for _ in range(n):
    point = Point()
    x=input().split()
    point.x=int(x[0])
    point.y=int(x[1])
    NBOX.append(point)

Start = NBOX[0]
End = NBOX[1]

MBOX = []
for _ in range(m):
    point = Point()
    x=input().split()
    point.x=int(x[0])
    point.y=int(x[1])
    MBOX.append(point)
