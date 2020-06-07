import urllib

plain = "https://en.wikipedia.org/wiki/Coppersmith%27s_attack"
encoded = urllib.parse.quote_plus(plain)
print(encoded)
