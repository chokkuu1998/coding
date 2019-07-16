xx,yy,zz=map(int,input().split())
count=0
for i in range(xx,yy+1):
   if str(zz)in str(i):
       count+=1
print(count)
