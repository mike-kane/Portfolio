# -*- coding: utf-8 -*-
######################################################################################################################
#                                                   Project Euler Problem 47 Solution -- Distinct Prime Factors
#                                                                       By Mike Kane
#
#  The first two consecutive numbers to have two distinct prime factors are:
#
#  14 = 2 × 7
#  15 = 3 × 5
#
#  The first three consecutive numbers to have three distinct prime factors are:
#
#  644 = 2² × 7 × 23
#  645 = 3 × 5 × 43
#  646 = 2 × 17 × 19.
#
#  Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
#
######################################################################################################################

import pyprimes

def checkFactors(set1, set2, set3, set4):
    for num1 in set1:
        if num1 in set2 or num1 in set3 or num1 in set4:
            return True
    for num2 in set2:
        if num2 in set1 or num2 in set3 or num2 in set4:
            return True
    for num3 in set3:
        if num3 in set1 or num3 in set2 or num3 in set4:
            return True
    for num4 in set4:
        if num4 in set1 or num4 in set2 or num4 in set3:
            return True
    return False

def getAnswer():
    x = 647
    while True:
        set1 = set(pyprimes.factors(x))
        set2 = set(pyprimes.factors(x+1))
        set3 = set(pyprimes.factors(x+2))
        set4 = set(pyprimes.factors(x+3))
        if len(set1) == 4 and len(set2) == 4 and len(set3) == 4 and len(set4) == 4:
            if checkFactors(set1, set2, set3, set4) == True:
                return x, x+1, x+2, x+3
        else:
            x += 1
    