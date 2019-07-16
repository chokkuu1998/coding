    
num=int(input())
elements=list(map(int,input().split()))
l=[]
for value in range(num):
    if elements[value]==value:
        l.append(str(value))
        l.sort()
if len(l)==0:
    print("-1")
print(" ".join(l))
