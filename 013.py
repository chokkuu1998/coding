# your code goes here
from itertools import permutations
ss=input()
kk=permutations(ss)
l=[]
m=(-1)
a="abcdefghijklmnopqrstuvwxyz"
if a==ss:
  print(ss)
elif ss==a[::-1]:
  print("-1")
else:
	ss=tuple(ss)
	for i in kk:
		l.append(i)
	for i in l:
		if i>ss:
			m=i
			break

	for i in l:
		if i>ss and i<m:
			m=i

	if m==-1:
		print("-1")
	else:
		for i in m:
			print(i,end="")
