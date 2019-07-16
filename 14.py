MM=int(input())
xx=[int(i) for i in input().split()]
while len(xx)!=0:
	n=len(xx)
	y=len(xx)//2
	if n%2==1:
		print(xx[y])
		xx.remove(xx[y])
	else:
		MM=(xx[y]+xx[y-1])//2
		print(MM)
		xx.remove(xx[y])
		xx.remove(xx[y-1])
