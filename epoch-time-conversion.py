import time

sec = 12345678

print(sec)
print(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(sec)))
