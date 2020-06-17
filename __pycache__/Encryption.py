import generatePrime
import findN
import findMultiplicativeInverse
import findCoPrime
import EdwardRule
import Decryption

#x is not 0 and y is not +-1

#prints out the crypted message. Returns the secret key that can be used to decrypt the message

def encrypt(x, y):
    p = generatePrime.findPrime()
    #print("p: {0}".format(p))
    q = generatePrime.findPrime()
    while p == q:
        q = generatePrime.findPrime()
    #print("q: {0}".format(q))
    N = findN.getN(p, q)
    print("N: {0}".format(N))
    n = (p+1)*(q+1)
    e = findCoPrime.findCoPrime(p, q)
    print("e: {0}".format(e))
    k = findMultiplicativeInverse.modInverse(e, n)
    print("k: {0}".format(k))
    M = (x, y)
    print("M: {0}".format(M))
    d = ((y**2 - 1) * findMultiplicativeInverse.modInverse((y**2 + 1)* x**2, N)) % N
    print("d: {0}".format(d))
    C = EdwardRule.EdwardMultiply(M, e, d, N)
    print ("C: {0}".format(C))
    return C

encrypt(1,2)


