##########################################################################################################
#  Project Euler Problem 7 Solution -- 10001st Prime
#  By Mike Kane
#
#  By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#  What is the 10 001st prime number?
#
##########################################################################################################

from helper_functions import primeSieve
import time

start = time.time()

def getAnswer():
    '''
        I'm being a little wasteful here, in the interest time.

        1) Generate all primes below a 1 million.
        2) return the 10,001 item in the list.

        This isn't technically the best answer, because I can't be sure the 10,001st
        prime isn't greater than 1M, which means I may have to guess and check a little.
     '''

    x = primeSieve(1000000)
    return x[10000]

if __name__ == "__main__":
    print("answer is {}, found in {} seconds.".format(getAnswer(), time.time() - start))

# answer is 104743, found in 0.6514890193939209 seconds.    
