# Write a function to compute 5/0 and use try/except to catch the exceptions.
#
# Hints:
#
# Use try/except to catch exceptions.
#
try:
    a = int(input("a"))
    b = int(input("b"))
    def func(a,b):
        return a//b
except ValueError:
    print("enter only numbers")
except ZeroDivisionError:
    print("The vlaue of b cant be 0")
print(func(a,b))