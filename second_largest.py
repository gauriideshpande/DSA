n = input().split(" ")
num=[]

for i in range(0, len(n)):
    num.append(int(n[i]))

largest = 0
s_largest = 0

for i in num:
    if i > largest:
        s_largest = largest 
        largest = i 
    elif i < largest and i > s_largest:
        s_largest = i
        
print(largest, s_largest)