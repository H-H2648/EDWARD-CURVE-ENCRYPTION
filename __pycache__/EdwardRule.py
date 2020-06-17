import findMultiplicativeInverse
import findCoPrime
#x = (x0, y0) and y = (x1, y1)
def EdwardSum(x, y, d, N):
    if (-d* x[0]**2 + x[1]**2) % N != (1 + d * x[0]**2 * x[1]**2) % N:
        print("SOMETHING IS WRONG STOP")
        print(d, x[0], x[1])
        print(-d* x[0]**2 + x[1]**2)
        print(1 + d * x[0]**2 * x[1]**2)
        print(x)
    if (-d* y[0]**2 + y[1]**2) % N != (1 + d * y[0]**2 * y[1]**2) % N:
        print("SOMETHING IS WRONG STOP")
        print(d, y[0], y[1])
        print(-d * y[0] ** 2 + y[1] ** 2)
        print(1 + d * y[0] ** 2 * y[1] ** 2)
        print(y)
    if not findCoPrime.coprime(1 + d*x[0]*y[0]*x[1]*y[1], N):
        print((1 + d*x[0]*y[0]*x[1]*y[1], N))
    if not findCoPrime.coprime(1 - d*x[0]*y[0]*x[1]*y[1], N):
        print((1 - d*x[0]*y[0]*x[1]*y[1], N))

    x1 = ((x[0]*y[1] + x[1]*y[0])*(findMultiplicativeInverse.modInverse(1 + d*x[0]*y[0]*x[1]*y[1], N))) % N
    y1 = ((y[1]*x[1] + d * x[0]*y[0])*(findMultiplicativeInverse.modInverse(1 - d*x[0]*y[0]*x[1]*y[1], N))) % N
    return ((x1, y1))

def EdwardDouble(x, d, N):
    return EdwardSum(x, x, d, N)

def EdwardSumList(list, d, N):
    SUM = (0, 1)
    for point in list:
        SUM = EdwardSum(SUM, point, d, N)
    return SUM

#computes N(x1, y1)
def EdwardMultiply(x, e, d, N):
    binary_e = []
    while e!= 0:
        bit = e % 2
        binary_e.append(bit)
        e = e//2
    SUMTOLIST = []
    for bit in binary_e:
        if bit == 1:
            SUMTOLIST.append(x)
        x = EdwardDouble(x, d, N)
    return(EdwardSumList(SUMTOLIST, d, N))



