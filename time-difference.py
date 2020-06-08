import datetime

now = datetime.datetime.now() # (or .utcnow())
then = datetime.datetime.strptime('2000-1-1 11:11:11', '%Y-%m-%d %H:%M:%S')
print('That was ' + str(now-then) + ' ago')
