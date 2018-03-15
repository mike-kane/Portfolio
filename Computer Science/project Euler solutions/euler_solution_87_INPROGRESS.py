##########################################################################################################################################################################################
#                                           Project Euler Problem 87 Solution -- Prime Power Triples
#
#
#
#  The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28.
#
#  In fact, there are exactly four numbers below fifty that can be expressed in such a way:
#
#  28 = 22 + 23 + 24
#  33 = 32 + 23 + 24
#  49 = 52 + 23 + 24
#  47 = 22 + 33 + 24
#
#How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
##########################################################################################################################################################################################
import pyprimes, time


def getPrimes(number):
    primeList = list(pyprimes.primes_below(number))
    return primeList
    
def getAnswer():
    start = time.time()
    number = 0
    answerList = []
    primeSquares = getPrimes(8000)
    primeCubes = getPrimes(205)
    primeQuads = getPrimes(85)
    for square in primeSquares:
        for cube in primeCubes:
            for quad in primeQuads:
                number = square**2 + cube**3 + quad**4
                print number
                if number < 50000000:
                    if number not in answerList:
                        answerList.append(number)
                    else:
                        print str(number) + "            REPEAT!!!"
    print len(answerList)
    print "Total Runtime: " + str(time.time() - start)
    
    
