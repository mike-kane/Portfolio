######################################################################################
# Project Euler Problem 10 Solution
# By Mike Kane
#
# Summation of Primes
#
# The sum of all primes below 10 is 2 + 3 + 5 + 7 = 17self.
#
# Find the sum of all primes below 2 million.
#
######################################################################################

from helper_functions import primeSieve as ps
import time
start = time.time()

def getAnswer():

    primes = ps(2000000)
    return sum(primes)



if __name__ == "__main__":
    print("answer is {}, found in {} seconds.".format(getAnswer(), time.time() - start))
