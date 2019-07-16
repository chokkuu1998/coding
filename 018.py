import sys,string
def dgtSum(nn) :
    sum1 = 0
    while nn :
        sum1 += nn%10
        nn //= 10
    return sum1

nn = int(input())
if nn <= 9:
    print(nn)
    sys.exit()
aa = nn // 9
bb = nn % 9
if bb :
    s = str(bb) + str('9') * aa
else :
    s = str('9') * aa
print(s)
