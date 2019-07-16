zz=int(input())
aa=list(map(int,input().split()))
ll=[]
for i in range (zz):
    if(aa[i]==i):
        l.append(i)
if(len(l)!=0):
    print(*l)
else:
    print('-1')
