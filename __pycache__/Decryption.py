import EdwardRule

#return the original message
def Decrypt(x, y, key, d, N):
    C = (x, y)
    M = EdwardRule.EdwardMultiply(C, key, d, N)
    #print(M)
    return M

print(Decrypt(2801985714, 5251984320, 327031499, 5140941083, 6426176353))



