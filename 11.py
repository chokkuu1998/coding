ssm = int(input())
llr = list(map(int,input().split()))
for i in range(len(llr)-1):
    if llr[i]>llr[i+1]:
        print(llr[i+1],end=" ")
    else:
        print(-1,end=" ")
print(-1)
