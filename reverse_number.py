# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# # -231 <= x <= 231 - 1
# import math

# n = int(input())
# lst = list(map(int, str(n)))
# def reverseNumber(n):
#     i = len(lst)-1
#     ans = []
#     if lst[0] == "-":
#         ans.append(lst[0])
#         while(i>0):
#             ans.append(lst[i])
#             i -= 1
#     else:
#         while(i>=0):
#             ans.append(lst[i])
#             i -= 1
#     print(int("".join(map(str, ans))))
        
        

# reverseNumber(n)
x  = input()
print(x[::-1])
