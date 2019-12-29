def stringToBit(string):
    for n in string:
        string = string + str(ord(n))
    print(bin(int(string)))

stringToBit("randomString")
