from functools import reduce
def find_gcd(x, y):
    while y:
        x, y = y, x % y

    return x

#print(reduce(find_gcd, (15,25,35,45)))


def gcd(x, y, *args):
    if len(args) > 0:
        res = find_gcd(x,y)
        for i in args:
            res = find_gcd(res,i)
        return res
    else:
        return find_gcd(x,y)

print(gcd(25,35,45,55))