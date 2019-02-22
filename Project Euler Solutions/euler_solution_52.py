############################################################################################################################################
#                                   Project Euler Problem 52 Solution -- Permuted Multiples
#                                                           By Mike Kane
#
#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
#
############################################################################################################################################

def digitChecker(number1, number2, number3, number4, number5, number6):
    number1 = list(str(number1))
    number2 = list(str(number2))
    number3 = list(str(number3))
    number4 = list(str(number4))
    number5 = list(str(number5))
    number6 = list(str(number6))
    number1.sort()
    number2.sort()
    number3.sort()
    number4.sort()
    number5.sort()
    number6.sort()
    
    numberList = [number1, number2, number3, number4, number5, number6]
    
    for number in numberList:
        if number != number1:
            return False
    return True
    
    
def getAnswer():
    number = 1
    num2x = number * 2
    num3x = number * 3
    num4x = number * 4
    num5x = number * 5
    num6x = number * 6
    
    while digitChecker(number, num2x, num3x, num4x, num5x, num6x) != True:
        number += 1
        num2x = number * 2
        num3x = number * 3
        num4x = number * 4
        num5x = number * 5
        num6x = number * 6
        
    return number
    
    