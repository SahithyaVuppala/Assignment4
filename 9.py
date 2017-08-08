# #9.
# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
#
# Hints:
# Use Subclass(Parentclass) to define a child class.
#import Person, abstractmethod
class Person():
    def getGender(self):
        pass

class Male(Person):
    def getGender(self):
        return 'Male'
class Female(Person):
    def getGender(self):
        return 'Female'
p = Person()
a = Male()
b = Female()
print(a.getGender())
print(b.getGender())

print(p.help())