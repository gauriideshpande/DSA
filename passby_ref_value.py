# Geek is learning about functions and calling a function with arguments. He learns that passing can take one of two forms: pass by value or pass by reference.

# Geek wishes to add 1 and 2, respectively, to the parameter passed by value and reference. Help Geek in fulfilling his goal.

# Example 1:

# Input:
# a = 1
# b = 2
# Output:
# 2 4
# Explanation: 1 was passed by value whereas 2 passed by reference.
# Example 2:

# Input:
# a = 10
# b = 20
# Output: 11 22
# Explanation: 10 was passed by value whereas 20 passed by reference.

# Constraints:
# 1 <= a,b <= 105

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function passedBy() which takes a and b as input parameters and returns array of two required integers.

# Expected Time Complexity: O(1)
# Expected Auxiliary Space: O(1)
a = int(input())
b = []
b.append(input())

# In python, pass by reference only works with list and not with other datatypes.
# In C++, "&" can be used to pass by reference.

def passedByValue(a):
    a = a + 2
    print("a's value in function: ", a)

def passedByRef(b):
    b.append("i")
    print("b's value in function:", b)

passedByValue(a)
print("a's value after function: ", a)
passedByRef(b)
print("b's value after function: ", b)
