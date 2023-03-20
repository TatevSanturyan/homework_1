from datetime import datetime
from functools import  wraps
import logging
logging.basicConfig(filename='performance.log', format='%(asctime)s - %(message)s', level=logging.INFO)

def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = datetime.now()
        res = func(*args,**kwargs)
        logging.info(f"{func.__name__,*args} - {datetime.now() - start}")

        return res
    return wrapper

@timer
def factorial(x):
    res = 1
    for i in range(2, x + 1):
        res *= i
    return res

print(factorial(15))
