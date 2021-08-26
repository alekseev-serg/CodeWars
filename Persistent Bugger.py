def persistence(num):
    if num < 10:
        return 0
    num_str = str(num)
    total = 1
    for i in num_str:
        total = total * int(i)

    return 1 + persistence(total)


print(persistence(25))


# Simple
"""
def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count
"""