def factorial(x):
    total = 1
    while x != 1:
        total *= x
        x -= 1
    return total
    
def getCount(n, r):
    c = factorial(n)/(factorial(r) * factorial(n - r))
    return c


def getAnswer():
    totalCount = 0
    for n in range(2,101):
        print n
        for r in range(1, n - 1):
            if getCount(n, r) > 1000000:
                totalCount += 1
    return totalCount