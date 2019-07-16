ss=input()
nn=1
if len(ss)==1:
    print("yes")
else:
    for j in ss:
        if ss.count(j)==len(ss):
            print("no")
            n=0
            break
    if nn==1:
        print("yes")
