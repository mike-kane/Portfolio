import itertools

def getAnswer():
    counter = 0
    iteration = itertools.permutations('0123456789', 10)
    for num in iteration:
        counter += 1
        if counter == 1000000:
            return num

        