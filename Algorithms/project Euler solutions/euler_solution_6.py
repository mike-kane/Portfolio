# -*- coding: utf-8 -*-
##########################################################################################################################################################################
# Project Euler Problem 6 Solution -- Sum Square Difference
# By Mike Kane
#
#  The sum of the squares of the first ten natural numbers is,
#
#  12 + 22 + ... + 102 = 385
#  The square of the sum of the first ten natural numbers is,
#
#  (1 + 2 + ... + 10)2 = 552 = 3025
#  Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
#  Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#
##########################################################################################################################################################################
import time

def getSquareOfSum():
    sums = 0
    for x in range(1, 101):
        sums += x
    return sums**2

def getSumOfSquare():
    listOfSquares = []
    for x in range(1, 101):
        listOfSquares.append(x**2)
    sumOfSquares = 0
    for item in listOfSquares:
        sumOfSquares += item
    return sumOfSquares

def getAnswer():
    startTime = time.time()
    return "{} found in {} seconds.".format((getSquareOfSum()- getSumOfSquare()), time.time() - startTime)

 #'25164150 found in 0.000113010406494 seconds.'
