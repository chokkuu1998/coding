NN=int(input())
aa=[]
cc=0
for i in range(2,NN):
    for j in range(2,i+1):
        if i%j==0:
            break
    if j==i:
        aa.append(i)
for i in range(len(aa)):
    for j in range(len(aa)):
        for k in range(len(aa)):
            if aa[i]+aa[j]+aa[k]==N:
                print(str(aa[i])+" "+str(aa[j])+" "+str(aa[k]))
                cc=1
                break
        if cc==1:
            break
    if cc==1:
        break
