aa=int(input())
bb=list(map(str,input().split()))[:aa]
cc=input()
dd=0
for i in range(0,aa):
  if(bb[i].startswith(cc)):
    dd=dd+1
print(dd)
