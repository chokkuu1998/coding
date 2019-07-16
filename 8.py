a = input()

b = input()

s = ""

for i in range(len(a)):

    for j in range(len(a),-1,-1):
    
        if a[i:j] in b:
        
            if len(a[i:j])>=len(s):
            
                s=a[i:j]
print(s)
