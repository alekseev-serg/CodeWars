def odd_count(n):
    c = 0
    for i in range(0, n):
        if i % 2 != 0:
            c += 1
    return c


print(odd_count(7))


def oddcount(n):
    return n // 2
