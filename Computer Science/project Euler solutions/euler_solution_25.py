# -*- coding: utf-8 -*-
################################################################################
#                               Project Euler Problem 25
#                                   by Mike Kane
#
#The Fibonacci sequence is defined by the recurrence relation:
#
#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#Hence the first 12 terms will be:
#
#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144
#The 12th term, F12, is the first term to contain three digits.
#
#What is the first term in the Fibonacci sequence to contain 1000 digits?
#
#
###############################################################################


def lengthChecker(number):
    if len(str(number)) == 10000:
        return True
    else:
        return False

def fibGenerator():
    tempFib = 0
    lastFib = 0
    newFib = 1
    fibPositionCounter = 1
    while lengthChecker(newFib)  != True:
        tempFib = lastFib
        lastFib = newFib
        newFib = lastFib + tempFib
        fibPositionCounter += 1
    return (newFib, fibPositionCounter)
