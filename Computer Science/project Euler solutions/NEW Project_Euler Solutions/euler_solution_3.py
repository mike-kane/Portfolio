################################################################################################################
#  Project Euler Problem 3 Solution -- Largest Prime Factor
#  By Mike Kane
#
#  The prime factors of 13195 are 5, 7, 13 and 29.
#
#  What is the largest prime factor of the number 600851475143 ?
#
################################################################################################################

from helper_functions import primeSieve
import time
import math

start = time.time()

def findLargestPrimeFactor(number):
    numRange = int(math.sqrt(number)) + 1

    primeFactors = [i for i in primeSieve(numRange) if number % i == 0]
    return primeFactors[-1]

if __name__ == "__main__":
    print("answer is {}, runtime is {}".format(findLargestPrimeFactor(600851475143), time.time() - start))
