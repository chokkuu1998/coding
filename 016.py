def primeless(nn):
    ll=[]
    for k in range(2,nn):
        if k==2:
            ll.append(2)
        else:
            for i in range(2,k):
                if k%i==0:
                    break
            if i==k-1:
                ll.append(k)
    return l
nn=int(input())
ll=primeless(nn)
if(len(ll)>0):
    if(ll[-1] == 97):
        print(" ".join(map(str,ll)),"")
    else:
        print(" ".join(map(str,ll)))
else:
    print(0)
