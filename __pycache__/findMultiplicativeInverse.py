#computes modular inverse
def modInverse(e, N):
	try:
		return(pow(e, -1, N))
	except:
		print("THIS SHOULD HAVE NEVER HAPPENED")
		print(e)
		print(N)


