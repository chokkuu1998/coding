num=int(input())
num_input=input()
lis1=lis(map(int,num_input.split()))
lis1.sort(reverse=True)
s=[str(i) for i in lis1]
result=int("".join(s))
print(result)
