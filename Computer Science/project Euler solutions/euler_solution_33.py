##################################################################################################################################################################################################################
#                                                                               Project Euler Problem 33 Solution -- Digit Canceling Fractions
#                                                                                                           By Mike Kane
#
#  The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
#  We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
#  There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
#  If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
#
##################################################################################################################################################################################################################
from fractions import Fraction

def checkDigits(num, denom):
    num = int(num)
    denom = int(denom)
    if num % 10 == 0:
        return False
    if denom % 10 == 0:
        return False
    num = str(num)
    denom = str(denom)
    for char in num:
        if char in denom:
            return char
    return False


expected = 0.0
fractions = []
sharedNum = ''
tempNum = ''
tempDenom = ''
for num in range(11, 100):
    for denom in range(num + 1, 100):
        if num % 10 != 0 and denom % 10 != 0:
            sharedNum = checkDigits(num, denom)
            expected = float(num) / denom
            if sharedNum != False:
              tempnum = list(str(num))
              tempDenom = list(str(denom))
              tempnum.remove(sharedNum)
              tempDenom.remove(sharedNum)
              if expected == float(tempnum[0]) / float(tempDenom[0]):
                   fractions.append(expected)
answer = 1
for item in fractions:
    answer *= item
print answer
            