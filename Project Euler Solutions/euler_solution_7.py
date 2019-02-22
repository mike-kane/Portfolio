##########################################################################################################
#  Project Euler Problem 7 Solution -- 10001st Prime
#  By Mike Kane
#
#  By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#  What is the 10 001st prime number?
#
##########################################################################################################
import time, pyprimes

# BRUTE FORCE METHOD-- VERY INEFFICIENT

def checkPrime(number):
    for x in range(2, number/2 - 1):
        if number % x == 0:
            return False
    return True

def getAnswer():
    start = time.time()
    primeCounter = 6
    numToCheck = 15
    while primeCounter != 10001:
        numToCheck += 2
        if checkPrime(numToCheck):
            primeCounter += 1
        print numToCheck
    return '{} is the {} prime, found in {} seconds.'.format(numToCheck, primeCounter, time.time() - start)

 #'104743 is the 10001 prime, found in 51.6697640419 seconds.'   Under the Euler time limit of 1 minute, but very, very inefficient

#  Easiest method--Use a pre-existing library!

def quickAnswer(numPrime):
    start = time.time()
    counter = 1
    numToCheck = 3
    while counter != numPrime:
        if pyprimes.isprime(numToCheck):
            counter += 1
        numToCheck += 1
    return '{} is the 10001st prime, found in {} seconds.'.format(numToCheck - 1, time.time() - start)

#'104743 is the 10001st prime, found in 0.607132911682 seconds.'
