nn=int(input())
l=[int(i) for i in input().split()]
while nn!=0:
	if nn%2==0:
		aa=int(nn/2)
		bb=a-1
		avg=(l[aa]+l[bb])//2
		print(avg)
		l.remove(l[aa])
		l.remove(l[bb])
		nn=nn-2
	else:
		aa=(nn//2)
		print(l[aa])
		l.remove(l[aa])
		nn=nn-1
