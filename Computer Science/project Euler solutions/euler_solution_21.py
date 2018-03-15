# -*- coding: utf-8 -*-
#############################################################################################################################################################################################################################
#                                               Project Euler Problem 21 Solution--  Amicable Numbers
#
#
#
#  Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#  If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
#  For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
#  Evaluate the sum of all the amicable numbers under 10000.
#
#############################################################################################################################################################################################################################

def checkAmicableNumbers(number):
    divisorsList = []
    divisorsList2 = []
    for divisor in xrange(1, number/2 + 1):
        if number % divisor == 0:
            divisorsList.append(divisor)
    divisorSum = sum(divisorsList)
    
    
    for x in xrange(1, divisorSum/2 + 1):
        if divisorSum % x == 0:
            divisorsList2.append(x)
    
    if sum(divisorsList2) == number:
        return (True, number, divisorSum)
    else:
        return False
        

def getAnswer():
    amicableNumbersList = []
    amicableNumbersCheck = ()
    for x in xrange(1,10001):
        if checkAmicableNumbers(x) != False:
            amicableNumbersCheck = checkAmicableNumbers(x)
            if amicableNumbersCheck[1] != amicableNumbersCheck[2]:
                for item in amicableNumbersCheck:
                    if item!= True and item not in amicableNumbersList:
                        amicableNumbersList.append(item)
    return (amicableNumbersList, sum(amicableNumbersList))
            