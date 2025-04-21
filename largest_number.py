n = input().split(" ")
num=[]

for i in range(0, len(n)):
    num.append(int(n[i]))

largest = 0

for i in num:
    if i > largest:
        largest = i
        
print(largest)