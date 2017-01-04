################################################################################
#  Project Euler Problem 6 Solution -- Sum Square Difference
#  By Mike Kane
#
#  The sum of the squares of the first ten natural numbers is,
#
#  1**2 + 2**2 + ... + 10**2 = 385
#  The square of the sum of the first ten natural numbers is,
#
#  (1 + 2 + ... + 10)**2 = 552 = 3025
#  Hence the difference between the sum of the squares of the first ten natural
#  numbers and the square of the sum is 3025 − 385 = 2640.
#
#  Find the difference between the sum of the squares of the first one hundred
#  natural numbers and the square of the sum.
#
##########################################################################################################################################################################
import time

start = time.time()

def getAnswer(numRange=101):
    ''' List comprehensions make this one a one-liner!  Just subtract the sum of
        the squares comprehension from the square of the sums comprehension.
    '''

    return sum(i for i in range(numRange))**2 - sum([i**2 for i in range(numRange)])



if __name__ == "__main__":
    print("answer is {}, found in {} seconds.".format(getAnswer(), time.time() - start))

# answer is 25164150, found in 5.507469177246094e-05 seconds.
