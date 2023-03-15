def find_gcd(x, y):
    while (y):
        x, y = y, x % y

    return x


l = [5, 15, 25, 85]

num1 = l[0]
num2 = l[1]
gcd = find_gcd(num1, num2)

for i in range(2, len(l)):
    gcd = find_gcd(gcd, l[i])

print(gcd)


# second way
def gcd(my_list):
    result = my_list[0]
    for x in my_list[1:]:
        if result < x:
            temp = result
            result = x
            x = temp
        while x != 0:
            temp = x
            x = result % x
            result = temp
    return result


print(gcd([18, 16, 112]))
