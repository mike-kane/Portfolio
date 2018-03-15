################################################################################################################################################################################
#                                                           Project Euler Problem 37 Solution -- Truncatable Primes
#                                                                               By Mike Kane
#
#  The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#
#  Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
#  NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
#
#################################################################################################################################################################################

import pyprimes

def checkLeft(number):
    
    number = str(number)
    while len(number) > 1:
        if pyprimes.isprime(int(number)) != True:   # check to make sure number is still prime
            return False                            # return False because number is not still prime, therefore not a truncatable prime
        else:
            number = number[1:]                     # remove far left digit
    if pyprimes.isprime(int(number)) == True:
        return True
    else:
        return False

def checkRight(number):
    
    number = str(number)
    while len(number) > 1:
        if pyprimes.isprime(int(number)) != True:   # check to make sure number is still prime
            return False                            # return False because number is not still prime, therefore not a truncatable prime
        else:
            number = number[:-1]                    # remove far right digit
    if pyprimes.isprime(int(number)) == True:
        return True
    else:
        return False
            
    

def getAnswer():
    truncPrimes = []
    primes = list(pyprimes.primes_below(1000000))
    primes = primes[::-1]
    
    for prime in primes:
        if len(truncPrimes) == 11:
            return sum(truncPrimes)
        if checkLeft(prime) and checkRight(prime):
            truncPrimes.append(prime)
    
