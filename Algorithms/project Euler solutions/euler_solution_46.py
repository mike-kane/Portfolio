# -*- coding: utf-8 -*-
################################################################################################################################
#                                   Project Euler Problem 46 Solution -- GoldBach's Other Conjecture
#                                           By Mike Kane
#
#  It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
#  9 = 7 + 2×1**2
#  15 = 7 + 2×2**2
#  21 = 3 + 2×3**2
#  25 = 7 + 2×3**2
#  27 = 19 + 2×2**2
#  33 = 31 + 2×1**2
#
#  It turns out that the conjecture was false.
#
#  What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
#
################################################################################################################################
import pyprimes, time

start = time.time()

def doubleOfSquares():
    doubleOfSquaresList = []
    number = 1
    while number != 1000000:
        doubleOfSquaresList.append((number**2) * 2)
        number += 1
    return doubleOfSquaresList
    
squaresList = doubleOfSquares()
print squaresList[-1]    
def listOfPrimes(number):
    x = list(pyprimes.primes_below(number))
    return x

primeList = listOfPrimes(2000000)
print primeList[-1]
    
def checkGoldbach(number):
    if number % 2 == 0:
        return False
    if number in primeList:
        return False
    for square in squaresList:
        if square < number:
            for prime in primeList:
                if prime < number:
                    if square + prime == number:
                        return False    # shows that this Goldbach Conjecture is true for this statement--not the answer I need
    return True

def getAnswer():
    counter = 33
    while checkGoldbach(counter) != True:
        counter += 1
    return counter
        