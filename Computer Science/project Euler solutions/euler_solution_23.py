################################################################################################################################################################
#                                               Project Euler Problem 23 Solution -- Non-Abundant Sums
#                                                                   By Mike Kane
#
#  A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, 
#
#  the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
#  A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
#  As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
#
#  By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit 
#
#  cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is 
#
#  less than this limit.
#
#  Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#
################################################################################################################################################################
import time


def checkAbundant(number):
    
    divSum = 0
    for x in range(1, number/2 + 1):
        if number % x == 0:
            divSum += x
    return divSum > number

def getAnswer():
    start = time.time()
    '''generate list of abundant numbers between 1, 28123.
    
       
    '''
    temp = 0
    abundantNumList = list(x for x in range(28123) if checkAbundant(x))
    numList = set(x for x in xrange(28123))
    
    for x in abundantNumList:
        for y in abundantNumList:
            temp = x + y
            if temp > 28123:
                break
            if temp in numList:
                numList.remove(temp)
    print time.time() - start        
    return sum(numList)
    
    
    
                
    
    
    
        


















