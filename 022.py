import sys
def prime(nn):
    ss=0
    if nn==2: return 2
    else:
        for i in range(2,nn):
            if nn%i==0: ss=ss+1
    if ss==0: return nn
nn=int(input())
p=[]
for i in range(2,nn):
    x = (prime(i))
    if x != None: p.append(x)
for i in range(0,len(p)-1):
    for j in range(i+1,len(p)):
        if p[i]+p[j]==nn:
            print(p[i],end=" ")
            print(p[j])
            sys.exit()
