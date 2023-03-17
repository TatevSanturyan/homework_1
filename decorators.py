from datetime import datetime
from time import sleep

def timer(func):
    def wrapper(*args,**kwargs):
        start = datetime.now()
        res = func(*args,**kwargs)
        print(start,func, datetime.now() - start)

        return res
    return wrapper