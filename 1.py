# #1.
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#
# Hints:
# Use __init__ method to construct some parameters
#

class Sample:
    pass
    def __init__(self):
        self.input = input
    def getString(self):
        self.input = input()
    def printString(self):
         print(self.input.upper())
sample = Sample()
sample.getString()
sample.printString()