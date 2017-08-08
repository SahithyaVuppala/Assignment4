# #4.
# Question:
# Define a class named American which has a static method called printNationality.
#
# Hints:
#
# Use @staticmethod decorator to define class static method.
#
#
class American :
    def __init__(self,nationality):
        self.nationality = nationality
    @staticmethod
    def printNationality(nationality):
        print("Nationality :",nationality)
a = American("Indian")
a.printNationality(a)
