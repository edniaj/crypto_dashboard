import pytz
import time
import datetime


def main(test,**kwargs):
    print('test :',test)
    print(kwargs)

dict_ = {'data': 'a', 'pload': 'b'}

time = datetime.datetime.now(tz=pytz.timezone('UTC'))
print(time)
print(pytz.timezone('Singapore'))

t = '2019-03-01T02: 59: 31.000Z'
x = datetime.datetime.fromisoformat(t[:13])
# x = arrow.now('US/Pacific')
print(x)

x = set()
x.add(('a','b'))
print(('a','b') in x)
print(('b','a') in x)
x = time.now()
print(time.now() - x)