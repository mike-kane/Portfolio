# -*- coding: utf-8 -*-
############################################################################################################
#              Project Euler Problem 14 -- Longest Collatz Sequence
#
#
#  The following iterative sequence is defined for the set of positive integers:
#
#  n → n/2 (n is even)
#  n → 3n + 1 (n is odd)
#
#  Using the rule above and starting with 13, we generate the following sequence:
#
#  13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#  It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
#
#  Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
#  Which starting number, under one million, produces the longest chain?
#
#  NOTE: Once the chain starts the terms are allowed to go above one million.
#
#############################################################################################################


def returnCollatzCount(number):
    count = 0
    while number != 1:
        if number % 2 == 0:
            number = number /2
        else:
            number = (number * 3) + 1
        count += 1
    return count
    

def getAnswer():
    numberToCheck = 0
    longestChainLength = 0
    answer = 0
    for number in range (2, 1000001):
        numberToCheck = returnCollatzCount(number)
        if numberToCheck > longestChainLength:
            longestChainLength = numberToCheck
            answer = number
            print "Number:  " + str(answer) + "     Chain Length:    " + str(longestChainLength)
            

    
        

        