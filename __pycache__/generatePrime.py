import random
#finds a 5 digit prime number

def findPrime():
    f = open("APPROPRIATE_PRIME_LIST.txt", "r")
    g = list(f)
    return int(random.choice(g[:-1]))
    f.close()

