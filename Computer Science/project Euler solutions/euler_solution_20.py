# -*- coding: utf-8 -*-
###############################################################################
#
#                           Project Euler Problem 20 Solution
#                                       By Mike Kane
#
#
#   n! means n × (n − 1) × ... × 3 × 2 × 1
#
#   For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#   and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
#   Find the sum of the digits in the number 100!
#
#
###############################################################################

def getFactorial(number):
    total = 1
    while number > 1:
        total *= number
        number -= 1
    return total
    
def getAnswer():
    answer = 0
    number = str(getFactorial(100))
    for x in number:
        answer += int(x)
    return answer


