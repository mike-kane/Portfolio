######################################################################################
#                   Project Euler Problem 9 Solution --  Special Pythagorean Triplet
#                               Project Euler Problem 9
#
#  A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
#  a**2 + b**2 = c**2
#  For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.
#
#  There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#  Find the product abc.
######################################################################################
import time

start = time.time()
def getAnswer():

    for a in range(1, 1000):
        for b in range(2, 1000):
            for c in range(3, 1000):

                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    return "answer is {}.  Triplets are {}, {}, and {}. Runtime is {} seconds.".format(a*b*c, a, b, c,  time.time() - start)

if __name__ == "__main__":
    print(getAnswer())

# answer is 31875000.  Triplets are 200, 375, and 425. Runtime is 21.565988063812256 seconds.
