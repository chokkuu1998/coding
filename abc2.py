from itertools import combinations
nn,kk,mm=map(int,input().split())
lis=list(map(int,input().split()))
hh=list(combinations(lis,kk))
for i in range(0,len(hh)):
    yy=list(hh[i])
    zz = 0
    for j in range(0,kk):
        zz=zz+yy[j]
    if zz==mm:
        print("YES")
        sys.exit()
print("NO") 
