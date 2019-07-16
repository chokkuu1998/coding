nn=int(input())
l=[]
for i in range(nn):
	l1=[int(x) for x in input().split()]
	mm=sum(l1)
	l.append(mm)
mm=sum(l)/(nn*nn)
print("%.6f" %mm)
