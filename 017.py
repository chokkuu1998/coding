import math
def isprime(yy):
    if(yy==2):
        return True
    elif(yy%2 == 0):
        return False
    else:
        for j in range(2,int(math.sqrt(yy)+1)):
            if(y%j == 0):
                return False
        return True
nn = int(input(""))
prime = []
for i in range(2,nn):
    if(isprime(i)):
        prime.append(i)
if(len(prime)>0):
    if(prime[-1] == 97):
        print(" ".join(map(str,prime)),"")
    else:
        print(" ".join(map(str,prime)))
else:
    print(0)
