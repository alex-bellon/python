# Needs the brackets or else each entry will be \x00 * n
all_bytes = [bytes([i]) for i in range(256)]
