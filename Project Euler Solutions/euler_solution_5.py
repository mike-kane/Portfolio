############################################################################################################################################
#                                     project euler problem 5 Solution -- Smallest Multiple  
#                                                       By Mike Kane
#
#     2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#     What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
############################################################################################################################################
import time

def checkDivisibility(number, divisor):
    if number % divisor:
        return True
    else:
        return False

def getAnswer():
    startTime = time.time()
    counter = 5040   #if evenly divisible by all numbers 1-20, answer must be divisible by all numbers 1-10, and there a multiple of 2520 (LCM of 1-10)
    multiple = 11
    while multiple != 21:
        if counter % multiple == 0:
            multiple += 1   
        else:
            counter += 2520
            multiple = 11
            
    return "{} found in {} seconds".format(counter, time.time() - startTime)
    
#232792560 found in 0.0302658081055 seconds'
