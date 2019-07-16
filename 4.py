nn=int(input())
aa=list(map(int,input().split()))[:nn]
bb=min(aa)
cc=max(aa)
bb=aa.index(bb)+1
cc=aa.index(cc)+1
print(bb,cc)
