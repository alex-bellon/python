a = str.encode("hello")
b = str.encode("lsdfj")

print(a)
print(b)

result = ''
for i in range(len(a)):
    letter = a[i] ^ b[i]
    print(letter)
    result += chr(letter)

print(result.encode())
