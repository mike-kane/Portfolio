################################################################################
#                           Project Euler Problem 50 Solution
#                                   by Mike Kane
#
#   The prime 41, can be written as the sum of six consecutive primes:
#
#   41 = 2 + 3 + 5 + 7 + 11 + 13
#   This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
#   The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
#   Which prime, below one-million, can be written as the sum of the most consecutive primes?
################################################################################

import pyprimes
pyprimes.primes_below(1000000)
primesList = []

for x in pyprimes.primes_below(1000000):
    primesList.append(x)

def getAnswer():
    ''' program needs to check to see if any combination of prime numbers from list adds up to equal primeToBeChecked '''
    flippedPrimesList = reversed(primesList)
    numberToCheck = 0
    
    for number in flippedPrimesList:
        while numberToCheck < number:
            pass


def testSolution():
    primeTestNumber = 41
    testTotal = 0
    primeTestList = [1,2,3,5,7,11,13,17,19,23,29,31,37]
    consecutivePrimes = []
    startingPosition = 0
    

        
        
    
    
        
    
    
