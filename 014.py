tt=input()
ss=""
nn=0
for i in range(len(tt)):
    if tt[i]==" ":
        ss=ss+tt[i]
    elif  nn%2!=0:
        ss=ss+tt[i]
        nn=nn+1 
    else:
        ss=ss+tt[i].upper()
        nn=nn+1
print(ss)
