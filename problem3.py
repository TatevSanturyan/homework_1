from functools import reduce
def find_gcd(x, y):
    while y:
        x, y = y, x % y

    return x

print(reduce(find_gcd, (15,25,35,45)))
