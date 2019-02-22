####################################################################################
#                       Project Euler Problem 48 Solution
#                           by Mike Kane
#
#
#   The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
#
#   Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
#
####################################################################################

def getSelfPower(number):
    return number**number
    
def getAnswer():
    answer = 0
    for x in range(1, 1001):
        answer += getSelfPower(x)
    answer = str(answer)
    return answer[-10:]
