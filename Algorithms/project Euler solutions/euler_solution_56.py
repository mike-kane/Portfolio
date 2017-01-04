################################################################################################################################################
#                           Project Euler Problem 56  -- Powerful Digit Sums
#                                               By Mike Kane 
#
#  A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros.
#
#  Despite their size, the sum of the digits in each number is only 1.
#
#  Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?
#
################################################################################################################################################

def getAnswer():
    digitalSum = 0
    tempSum = 0
    for a in range(0, 100):
        for b in range(0, 100):
             tempSum = 0
             number = a**b
             number = str(number)
             for char in number:
                 tempSum += int(char)
                 if tempSum > digitalSum: digitalSum = tempSum
    return digitalSum
   