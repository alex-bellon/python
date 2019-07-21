import binascii

aHex = input('Input the hex string: ')
a = binascii.unhexlify(aHex)
print(a)
