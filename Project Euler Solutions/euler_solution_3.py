################################################################################################################
#                                               Project Euler Problem 3 Solution -- Largest Prime Factor
#                                                                       By Mike Kane
#
#  The prime factors of 13195 are 5, 7, 13 and 29.
#
#  What is the largest prime factor of the number 600851475143 ?
#
################################################################################################################

def factorFinder(x):
    '''
    expects an int as input.
    Returns a list of all factors for x.
    '''
    factorList = []     
    
    for number in range(1, int((x**.5)+1)):
        if x % number == 0:
           factorList.append(number)
   
    return factorList 
           
def primeChecker(x):
    '''
    expects an int as input for x.
    Returns a bool if number input number is determined to be prime.
    '''
    if x == 1:
        return False
    for number in range(2, (x/2) + 1):
        if (x % number) == 0:
            return False
    return True
                

def getAnswer(factorList):
    '''
    expects an array of integers as input.  
    --Checks to see if each integer is prime.
    --Returns largest prime in list.
    '''
    largestFactor = 1
    
    for item in factorList:
        if primeChecker(item):
            if item > largestFactor:
                largestFactor = item
    return largestFactor
    
print getAnswer(factorFinder(600851475143))

#answer = 6857