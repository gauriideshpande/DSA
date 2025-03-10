# While loop is another loop like for loop but unlike for loop it only checks for one condition.
# Here, we will use a while loop and print a number n's table in reverse order.

# Examples:

# Input: n = 1
# Output: 10 9 8 7 6 5 4 3 2 1
# Input: n = 2
# Output: 20 18 16 14 12 10 8 6 4 2
# Constraints:
# 1 <= n<= 1000

# Code starts from here.

n = int(input())

def reverseTable(n):
    i = 10
    ans = []
    while(i>=1):
        ans.append(n*i)
        i=i-1
    print(ans)
    # return ans

reverseTable(n)