from datetime import datetime
from time import sleep

def timer(func):
    def wrapper(*args,**kwargs):
        start = datetime.now()
        res = func(*args,**kwargs)
        print(start,func, datetime.now() - start)

        return res
    return wrapper


@timer
def factorial(x):
    res = 1
    for i in range(2, x + 1):
        res *= i
    return res

print(factorial(100))

