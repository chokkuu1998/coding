aa=input().split()
bb=[]
for i in aa:
  bb.append(i[::-1])
print(*bb)
