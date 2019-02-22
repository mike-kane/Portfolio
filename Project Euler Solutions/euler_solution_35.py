##############################################################################################################################
#                                           Project Euler Problem 35 Solution -- Circular Primes
#                                                           By Mike Kane
#
#  The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
#  There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
#  How many circular primes are there below one million?
#
##############################################################################################################################

import pyprimes

def checkPrime(number):
    number = int(number)
    if pyprimes.isprime(number) == True:
        return True
    else:
        return False

def makeRotation(number):
    number = list(str(number))
    rotation = number[-1]
    number = number[:-1]
    for char in number:
        rotation += char
    return rotation
    
def getAnswer():
    circPrimeCounter = 13    #for all circular primes below 100
    currentRotation = ''
    
    for x in range(100, 1000000):
        rotationList = []
        x = str(x)
        if '5' not in x and '2' not in x and '4' not in x and '6' not in x and '8' not in x:  #no need to check numbers containing evens or 5, since at least one rotation cannot be prime
            rotationList.append(x)
            currentRotation = makeRotation(x)
            rotationList.append(currentRotation)
            while len(rotationList) != len(x):
                currentRotation = makeRotation(currentRotation)
                rotationList.append(currentRotation)
            y = map(checkPrime, rotationList)
            if False not in y:
                circPrimeCounter += 1
    return circPrimeCounter
    
                
            
            
            
    
    
    
    
    