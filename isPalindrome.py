num = input().split()
lst = []
for i in num:
    lst.append(int(i))

revLst = lst[::-1]
if lst == revLst:
    print("Palindrome")
else:
    print("Not Palindrome")
