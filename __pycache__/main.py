import Encryption
import Decryption

def run():
    command = input("Encrypt or Decrypt?\n")
    while True:
        if command == "encrypt" or command == "Encrypt":
            x1 = int(input("x1:\n"))
            y1 = int(input("y1:\n"))
            C = Encryption.encrypt(x1, y1)
            command = input("Encrypt or Decrypt?\n")
        if command == "decrypt" or command == "Decrypt":
            x1 = int(input("x1:\n"))
            y1 = int(input("y1:\n"))
            key = int(input("secret key:\n"))
            d = int(input("d:\n"))
            N = int(input("N:\n"))
            M = Decryption.decrypt(x1, y1, key, d, N)
            print(M)
            command = input("Encrypt or Decrypt?\n")
        else:
            print("unknown command")
            command = input("Encrypt or Decrypt?\n")

run()