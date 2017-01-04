# -*- coding: utf-8 -*-
#########################################################################################################################################################
#                                           Project Euler problem 104 Solution -- Pandigital Fibonacci Numbers
#                                                                   By Mike Kane
#
#
#  The Fibonacci sequence is defined by the recurrence relation:
#
#  Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#
#  It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital 
#
#  (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the 
#
#  nine digits are 1-9 pandigital.
#
#  Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
#
##########################################################################################################################################################

def generateFibonacciNumbers():
    lastFib = 0
    midFib = 1
    newFib = 1
    fibList = []
    while len(str(newFib)) <  1900:
        lastFib = midFib
        midFib = newFib
        newFib = lastFib + midFib
        fibList.append(str(newFib))
    return fibList
    
def checkPandigital(number):
    number = str(number)
    number = list(number)
    listOfNumbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for num in number:
        if num in listOfNumbers:
            listOfNumbers.remove(num)
    if len(listOfNumbers) == 0:
        return True
    else:
        return False


def checkForAnswer():
    
    firstNine = ''
    lastNine = ''
    fibList = generateFibonacciNumbers()
    for goodFib in fibList:
        firstNine = goodFib[:9]
        lastNine = goodFib[::-1]
        lastNine = lastNine[:9]
        if checkPandigital(firstNine) == True and checkPandigital(lastNine) == True:
            return str(goodFib) + "    CORRECT!" 
        else:
            print str(goodFib) + " no...."
        
        
    
        
        
        
    