# coding: utf-8
# This program finds the maximum of two numbers.
# It uses the built-in max function.
# Can you do it with a conditional statement (if / if-else) instead?

x1 = float(input("number? "))
x2 = float(input("number? "))
x3 = float(input("number? "))

# Use a conditional statement instead of max function!
if x1 > x2 and x1 > x3:
    print("x1")
elif x2 > x1 and x2 > x3:
    print("x2")
elif x3 > x1 and x3 > x2:
    print("x3")
else:
    print("x3 or x2 or x1")
