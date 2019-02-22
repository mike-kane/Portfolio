# -*- coding: utf-8 -*-
########################################################################################################################################################################
#                                               Project Euler Problem 38 Solution -- Pandigital Multiples
#                                                                       By Mike Kane
#
#  293.36
#  lts
#  Take the number 192 and multiply it by each of 1, 2, and 3:
#
#  192 × 1 = 192
#  192 × 2 = 384
#  192 × 3 = 576
#  By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#
#  The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated 
#
#  product of 9 and (1,2,3,4,5).
#
#  What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
########################################################################################################################################################################

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
   '''range-- 193 - 333 ''' 
   
   largestPandigital = 0
   var1 = 0
   var2 = 0
   var3 = 0
   for x in range(193, 10000):
        if x < 334:
            strPandigital = ''
            var1 = x * 1
            var2 = x * 2
            var3 = x * 3
            strPandigital = str(var1) + str(var2) + str(var3)
        else:
            var1 = x * 1
            var2 = x * 2
            strPandigital = str(var1) + str(var2)
        if checkPandigital(strPandigital) ==True:
           print strPandigital
           if int(strPandigital) > largestPandigital:
               largestPandigital = int(strPandigital)
   return largestPandigital
   
       