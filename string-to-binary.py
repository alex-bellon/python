plain = input('Enter your string: ')
binary = ''.join(format(ord(x) , 'b').zfill(8) for x in plain)
print('String in binary: ' + binary)
