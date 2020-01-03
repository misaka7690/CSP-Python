para=list(input())
j=0
pa1=[]
pa2=[]
while j<len(para)-1:
    if para[j+1]==':':
        para.pop(j+1)
        para[j]+=':'
    else:
        j+=1
for p in para:
    if len(p)==2:
        pa2.append(p[0])
    else:
        pa1.append(p)

N=int(input())

for i in range(1,N+1):
    cmd=input().split()
    j=1
    ans=[]
    els={}
    # 没有参数，异常选项
    while j<len(cmd):
        if cmd[j][0]!='-':
            break
        if cmd[j][1] in pa1:
            ans.append(cmd[j])
            j+=1
        elif cmd[j][1] in pa2:
            if j+1==len(cmd):
                break
            else:
                if cmd[j+1] in pa1:
                    break
                else:
                    arg=cmd[j+1]
            ans.append(cmd[j])
            els[cmd[j]]=arg
            j+=2
        else:
            break
    ans=list(set(ans))
    ans.sort()
    j=0
    while j<len(ans):
        if ans[j][1] in pa2:
            ans.insert(j+1,els[ans[j]])
            j+=2
        else:
            j+=1

    print(f'Case {i}: '+' '.join(ans))
