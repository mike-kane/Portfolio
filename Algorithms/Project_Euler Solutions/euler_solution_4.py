#########################################################################################
#  Project Euler Problem 4 Solution -- Largest Palindrome Product
#  By Mike Kane
#
#  A palindromic number reads the same both ways. The largest palindrome made
#  from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#  Find the largest palindrome made from the product of two 3-digit numbers.
#
#########################################################################################

from helper_functions import isPalindrome
import time

def largestPalindromicProduct(min=100, max=999):
    '''
    1. creates a list comprehension of all products in range(100, 999) that are palindromic.

    2. returns largest.
    '''
    largest = 0
    list1 = [i for i in range(999, 100, -1)]
    list2 = list1
    for i in list1:
        for j in list2:
            product = i * j
            if isPalindrome(product):
                if product > largest:
                    largest = product
    return largest
if __name__ == "__main__":
    print(largestPalindromicProduct())

# Answer: 906609
