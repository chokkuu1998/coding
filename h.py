aa=input()
tt=0
ll=list(combinations(a,len(aa)-1))
for i in range(len(l)):
    if l[i]==l[i][::-1]:
        print("YES")
        t=1
        break
if t==0:
    print("NO")
