##############################################################################################################################################################################################
#                                       Project Euler Problem 41 Solution -- Pandigital Prime Numbers
#                                                           By Mike Kane
#
#
#  We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
#  What is the largest n-digit pandigital prime that exists?
#
##############################################################################################################################################################################################
import pyprimes

def checkPandigital(number):
    '''need to find length of number.   '''
    numList = ['1', '2', '3', '4', '5', '6', '7']
    number = str(number)
    numList = numList[:len(number)]
    numList = list(numList)
    number = list(number)
    numList.sort
    
    number.sort()
    
    if numList == number:
        return True
    else:
        return False
        
def getAnswer():        
    primesList = list(pyprimes.primes_below(7654321))
    print "Primes list loaded..."
    primesList = primesList[::-1]
    print "Primes list reversed..."
    for prime in primesList:
        print prime
        if checkPandigital(prime) == True:
            return prime
    
    
    
    
    
     
    

    