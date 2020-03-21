import random, string

n = 5
print(''.join(random.choice(string.ascii_lowercase) for x in range(n)))
print(''.join(random.choice(string.ascii_uppercase) for x in range(n)))
print(''.join(random.choice(string.ascii_letters) for x in range(n)))
print(''.join(random.choice(string.punctuation) for x in range(n)))
print(''.join(random.choice(string.printable) for x in range(n)))
print(''.join(random.choice(string.hexdigits) for x in range(n)))
print(''.join(random.choice(string.digits) for x in range(n)))
