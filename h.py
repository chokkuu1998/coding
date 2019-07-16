from itertools import combinations
pp=input()
qq=0
ll=list(combinations(pp,len(pp)-1))
for i in range(len(l)):
         if(l[i]==l[i][ ::-1]):
             print("YES")
             qq=1
             break
if(qq==0):
    print("NO")
