# -*- coding: utf-8 -*-
#########################################################################################
#  Project Euler Problem 4 Solution -- Largest Palindrome Product
#  By Mike Kane
#
#  A palindromic number reads the same both ways. The largest palindrome made
#  from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#  Find the largest palindrome made from the product of two 3-digit numbers.
#
#
#########################################################################################





import time

def find_max_palindrome(min=100,max=999):
    max_palindrome = 0                                                          # only concerned with max palindrome.  Do not need a list of all palindromes, only the largest
    a = 999                                                                     # set starting point for outside iterator
    while a > 99:                                                              # set exit condition for outside iterator
        b = 999                                                                 # set starting point for inside iterator.  This will run completely for each different outside iterator
        while b >= a:                                                           # Starts counting down from the top.  This way, less iterations to go through before running into the correct answer
            prod = a*b
            if prod > max_palindrome and str(prod)==(str(prod)[::-1]):          # checks to see if product is bigger that max_palindrome first. This is more likely to fail, saving time and resources
                max_palindrome = prod
            b -= 1                                                              #decrements inside iterator first
        a -= 1                                                                  #decrements outside iterator once inside loop has completely ran for outside iterator
    return max_palindrome                                                       # returns value saved as max_palindrome

start = time.time()
L = find_max_palindrome()
elapsed = (time.time() - start)

print "%s found in %s seconds" % (L,elapsed)

#answer = 906609
