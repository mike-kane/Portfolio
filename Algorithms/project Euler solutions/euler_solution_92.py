# -*- coding: utf-8 -*-
#########################################################################################################################################################################
#                                                           Project Euler Problem 92 Solution -- Square Digit Chains
#                                                                           By Mike Kane
#
#
#  A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
#
#  For example,
#
#  44 → 32 → 13 → 10 → 1 → 1
#  85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
#
#  Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
#
#  How many starting numbers below ten million will arrive at 89?
#
##########################################################################################################################################################################

def getSquare(number):
    squaresList = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    return squaresList[number]

def getSquareDigit(number):
    number = str(number)
    total = 0
    for num in number:
        total += getSquare(int(num))
    return total

def checkNum(number):
    if number == 0:
        return 0
    else:
        while True:
            number = getSquareDigit(number)
    	    if number == 1:
        	return False
            elif number == 89:
                return True


def getAnswer(numRange):
    total = 0
    
    for number in xrange(numRange):
        print number
        if checkNum(number) == True:
            total += 1            
            
    return total

