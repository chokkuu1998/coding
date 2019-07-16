NN=int(input())
ss=[]
for i in range(2,NN):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            if i%j!=0 and i+j==N:
                b=str(j)+' '+str(i)
                ss.append(str(b))
print(ss[-1])
