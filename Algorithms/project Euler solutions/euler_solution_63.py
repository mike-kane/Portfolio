############################################################################################################################################
#                           Project Euler Problem 63 -- Powerful Digit Counts
#
#
#  The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.
#
#  How many n-digit positive integers exist which are also an nth power?
#
#
#############################################################################################################################################

def getPowerfulDigitCount(number):
    power = 1
    counter = 0
    numToCheck = str(number**power)
    
    while len(numToCheck) >= power:
        if len(numToCheck) == power:
            counter += 1
        power += 1
        numToCheck = str(number**power)
    return counter

def getAnswer():
    
    counter = 0
    
    for num in range(2, 10):
        counter += getPowerfulDigitCount(num)
    return counter + 1
    
    
    
    
    

    
    