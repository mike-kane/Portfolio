#########################################################################################################################################################
#                                                   Project Euler Project 34 Solution -- Digit Factorials
#                                                               By Mike Kane
#
#
#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#
#########################################################################################################################################################

def getFactorial(number):
    total = 1
    
    while number >= 1:
        total *= number
        number -=  1
    return total

def getFactorialTotal(number):
    total = 0
    strNumList = list(str(number))
    for num in strNumList:
        total += getFactorial(int(num))
    return total
    
def getAnswer():
    total = 0
    
    for x in range(2540160):
        if getFactorialTotal(x) == x:
            total += x
            print x
    return total - 3
    