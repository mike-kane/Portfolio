################################################################################################
#                                   Project Euler Problem 1 Solution -- Multiples of 3 and 5
#                                                           By Mike Kane
#
# Determine the sum of all numbers < 1000 that are multiples of 3 or 5.
#
#
#################################################################################################
# Complexity: O(n)
import time

start = time.time()
def fizzBuzz(numRange):
    total = 0

    for number in range(numRange):
        if number % 3 == 0 or number % 5 == 0:
            total += number

    return total

#answer: 233168

if __name__ == "__main__":
    print("answer is {}, runtime is {} seconds".format(fizzBuzz(1000), time.time() - start))
