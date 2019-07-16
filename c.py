nn=int(input())
numm=list(map(int,input().split()))
l1=[]
for i in numm:
    if numm.count(i)>1:
        if str(i) not in l1:
            l1.append(str(i))
if len(l1)==0:
    print("unique")
else:
    numm.sort()
    print(" ".join(l1))
