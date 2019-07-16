nn,kk=map(int,input().split())
l=[str(x) for x in input().split()]
kk=str(kk)
a=" "
while kk in l:
    l.remove(kk)
if len(l)!=0:
    print(a.join(l))
else:
    print("empty")
