# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# ======================================================================================================
#

n = input()
sum= 0
for i in range(1,5):
    sum  += int(n*i)
print(sum)


lst = [1,2,6,12,4,5,3,7,8,9,10]
print([i for i in sorted(lst) if i%2 !=0] + [i for i in sorted(lst) if i%2 ==0])

arr = [1,2,6,12,4,5,3,7,8,9,10]
arr = sorted(arr, key=lambda x: (x % 2 == 0, x))
print(arr)


lst.sort()

