import random


#Finds gcd
#assumes a >= b
def gcd(a, b):
    while a % b != 0:
        a = a % b
        temp = a
        a = b
        b = temp
    return b



# Function to check and print if
# two numbers are co-prime or not
def coprime(a, b):
    return gcd(a, b) == 1

    # Driver code


#finds e, a number coprime to p^(r-1)(p+1)q^(s-1)(q+1)
#Assumes p and q are primes
def findCoPrime(p, q):
    n = (p+1)*(q+1)
    e = random.randint(1, n)
    while not coprime(n, e):
        e = random.randint(1, n)
    return e

