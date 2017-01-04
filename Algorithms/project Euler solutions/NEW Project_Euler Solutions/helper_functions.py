################################################################################
# Helper functions for Project Euler Solutions
#
# Written by Mike Kane
#
################################################################################

def iterFib(numRange):
    ''' returns a list of fibonacci numbers below the numRange argument.'''

    fibs = [1]
    fib1 = 0
    fib2 = 1
    newFib = 1

    while newFib < numRange:
        fib1, fib2 = fib2, newFib
        newFib = fib1 + fib2
        fibs.append(newFib)

    return fibs

def recurFib(n):
    ''' recursive fibonacci number generator.'''
    if n < 2:
        return 1

    return recurFib(n - 1) + recurFib(n - 2)

def primeSieve(numRange):
    '''basic sieve of Eratosthenes to generate prime numbers quickly.

        1. Begin by creating list of booleans for number in numRange
            - list comprehension starts at 2, since its the first prime numbers
            - comprehension automatically marks all even numbers as False, odd numbers as True
        2. Manually flip first bool since 2 is prime.
        3. Iterate through list
            -- if false, move on
            -- if true, get index
            -- divide numRange by index, save value in tempRange
            -- for x in 1, tempRange, tempNum = index * x
            -- set fullRange[tempNum] to False, since these numbers are multiples of original prime value
    '''
    fullRange = [False if i % 2 == 0 else True for i in range(2, numRange + 1)]
    primes = []
    fullRange.insert(0, False)
    fullRange.insert(2, True)
    for i, j in enumerate(fullRange):
        if j:
            primes.append(i)
            multipleOfIndex = i
            while (multipleOfIndex + i) < numRange:
                multipleOfIndex += i
                fullRange[multipleOfIndex] = False

    return primes


def isPalindrome(n):
    '''checks to see if input is a palindrome (reads same forwards and backwards)'''
    i = str(n)
    if len(i) == 0:
        return False
    else:
        return (i == i[::-1])

#if __name__ == "__main__":
#     import sys
#     x = sys.argv[1]
#     print(isPalindrome(x))
