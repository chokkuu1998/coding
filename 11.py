smm = int(input())
lrr = list(map(int,input().split()))
for i in range(len(lrr)-1):
    if lrr[i]>lr[i+1]:
        print(lrr[i+1],end=" ")
    else:
        print(-1,end=" ")
print(-1)
