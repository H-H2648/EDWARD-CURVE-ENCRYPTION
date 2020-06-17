import EdwardRule

#return the original message
def decrypt(x, y, key, d, N):
    C = (x, y)
    M = EdwardRule.EdwardMultiply(C, key, d, N)
    #print(M)
    return M




