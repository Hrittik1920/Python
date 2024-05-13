# # # Module Function e.g,
# # import math
# # from math import sqrt
# from math import *
# print(sqrt(16))


# User Define Function
# def  ---  Defination
# def print_sum(first,second=4):
#     print(first + second)

# print_sum(1,5)

def fib_recursive(num):
    if(num==1  or num==2):
        return num-1
    return fib_recursive(num-1) + fib_recursive(num-2)

print(fib_recursive(9))
