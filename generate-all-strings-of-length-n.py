import itertools, string

def generate_strings(length):
    chars = string.ascii_letters + string.digits
    for item in itertools.product(chars, repeat = length):
        yield "".join(item)

def main():
    for i in range(10): # Generate all strings from length 0-10
        gen = generate_strings(i)
        for string in gen:
            print(string)

main()
