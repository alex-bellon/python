import random

string = 'test'
shuffled = ''.join(random.sample(string, len(string)))

print(shuffled)
