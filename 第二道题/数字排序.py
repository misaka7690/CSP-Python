N=int(input())

data=list(map(int,input().split()))

from collections import Counter

data=Counter(data)

data=data.most_common()

data=list(map(lambda x: (x[1],x[0]),data))

data.sort(key=lambda x:x[0]*1000000-x[1])

data.reverse()

data=list(map(lambda x: (x[1],x[0]),data))

for i in range(len(data)):
    print(' '.join(map(str,data[i])))



