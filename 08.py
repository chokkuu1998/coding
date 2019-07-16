a=input()


a=list(a)

length=len(a)

s=[]

cit=1

for i in range(0,len(a)-2):

j=i+1 

if a[i]==a[j]:

a.remove(a[j])

if a[i] not in s:

s.append(a[i])

c=''.join(list(a))

k=''.join(list(s))

string=c+k

for i in range(0,len(string)-1):

j=i+1 

if string[i]!=string[j]:

cit=cit+1

#print(string[i])

#print(string[j])

#print(cit)

if cit==length:

print("yes")

else:

print("no")



