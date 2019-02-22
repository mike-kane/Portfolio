# -*- coding: utf-8 -*-
########################################################################################################################################################################################################################
#                                                       Project Euler Problem 32 -- Pandigital Multiples
#                                                                       By Mike Kane
#
#  We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234,
#
#  is 1 through 5 pandigital.
#
#  The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
#  Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
#  HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
#
########################################################################################################################################################################################################################

def checkPandigital(number):
    '''expects number as string '''
    numList = []
    numCheck = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for char in number:
        numList.append(char)
    numList.sort()
    if numList == numCheck:
        return True
    else:
        return False
        
def getAnswer():
    
    product = 0
    productSet = set()
    
    
    for multiplier in range(2000):
        for multiplicand in range(1000):
            pandigitalChecker = ''
            product = multiplier * multiplicand
            pandigitalChecker = str(multiplier) + str(multiplicand) + str(product)
            if checkPandigital(pandigitalChecker) == True:
                productSet.add(product)
    return sum(productSet)