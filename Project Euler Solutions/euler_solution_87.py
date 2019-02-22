###############################################################################################################################################
#                                       Project Euler Problem 87 Solution -- Prime Power Triplets
#                                                                   By Mike Kane
#
#  The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four 
#
#  numbers below fifty that can be expressed in such a way:
#
#  28 = 2**2 + 2**3 + 2**4
#  33 = 3**2 + 2**3 + 2**4
#  49 = 5**2 + 2**3 + 2**4
#  47 = 2**2 + 3**3 + 2**4
#
#  How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
#
###############################################################################################################################################



import pyprimes

def getAnswer():
    
    '''Generates a list of prime numbers up to the square root of upper bound (50 million)
    
    --3 nested loops each work through list of primes in primesList
    
    -- if prime**4 + prime**3 > upper bound, break inner loop. Else, add square. If still under 50 million, append to primeSet
    
    primeSet as set() ensures that there are no duplicates in final list.
    
    finally, returns length of prime set to get total number of prime numbers that can be represented as a prime power triplet.'''
    
    primesList = list(pyprimes.primes_below(int(50000000**0.5)))
    primeSet = set()
    for prime1 in primesList:
        for prime2 in primesList:
            num = prime1**3 + prime2**4
            if num >= 50000000:
                break
            for prime3 in primesList:
                checker = prime3**2 + num
                if checker >= 50000000:
                    break
                primeSet.add(checker)
    return len(primeSet)


    
    

    