nn=int(input())
lli=[]
sum=0
for i in range(nn):
  lli.append(list(map(int,input().split())))
for i in lli:
  sum+=sum(i)
print("{0:2f}".format((su/(nn*nn))))
