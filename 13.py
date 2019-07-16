from itertools import chain
from statistics import mean
nnn = int(input())
rrr = []
for _ in range(nnn):
    rrr.append(list(map(int, input().split())))
print(format((mean(chain.from_iterable(rrr))), '.6f'))
