################################################################################################################################
#                                   Project Euler Problem 36 Solution -- Double-Base Palindromes
#                                               By Mike Kane
#
#  The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
#  Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
#  (Please note that the palindromic number, in either base, may not include leading zeros.)
#
################################################################################################################################

def getBin(number):
    return int(bin(number)[2:])

def checkPalindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True
    else:
        return False

def getAnswer():
    total = 0
    binary = 0
    for number in xrange(1000000):
        if checkPalindrome(number) == True:
            binary = getBin(number)
            if checkPalindrome(binary) == True:
                total += number
    return total
    

    
    