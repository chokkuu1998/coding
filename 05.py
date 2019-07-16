nn=int(input())
l=[int(x) for x in input().split()]
c=0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]<l[j] and i<j:
            c+=1
print(c)
