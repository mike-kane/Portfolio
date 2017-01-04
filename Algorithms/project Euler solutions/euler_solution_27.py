# -*- coding: utf-8 -*-
############################################################################################################################################################################################
#
#
#
#
#  Euler discovered the remarkable quadratic formula:
#
#  n² + n + 41
#
#  It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, 
#
#  and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.
#
#  The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.
#
#  Considering quadratics of the form:
#
#  n² + an + b, where |a| < 1000 and |b| < 1000
#
#  where |n| is the modulus/absolute value of n
#  e.g. |11| = 11 and |−4| = 4
#  Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
#
#
############################################################################################################################################################################################

import pyprimes,time

def getAnswer():
    start = time.time()
    primesList = list(pyprimes.primes_below(1000))    #  B must be a prime number since the equation still outputs a prime when n = 0.
    highestPrimeCount = 0
    bestA = 0
    bestB = 0
    
    for a in range(-1000, 1000, 1):    
        for b in primesList:
            n = 0
            answer = (n**2 + a*n + b)   
            while pyprimes.isprime(answer) == True:                 #iterates through consecutive n values as long as the equation keeps spitting out a prime number
                n += 1
                answer = (n**2 + a*n + b)
            if n > highestPrimeCount:                               #checks to see if value of n is highest so far.  If so, reassigns highestPrimeCount to value of n, and keeps track of A and B values that generated this
                highestPrimeCount = n
                bestA = a
                bestB = b
    return "Total consecutive primes:  {}    A value:  {}    B Value:  {}    Product of coefficients:  {}   Solution found in {} seconds ".format(highestPrimeCount, bestA, bestB, (bestA * bestB), time.time() - start)
            
                
    
    