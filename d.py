ekk=int(input())
akk=input("")
ckk=list(akk.split(" "))
ckk.sort(reverse=True)
bkk=list(map(int,ckk))
if sum(bkk)==0:
  print("0")
else:
  dkk="".join(ckk)
  print(dkk)
