def sum_mul(n, m):
    s = 0
    if not isinstance(n, int) or not isinstance(m, int):
        return 'INVALID'

    if n <= 0 or m <= 0:
        return 'INVALID'

    for i in range(n, m):
        if i % n == 0:
            s += i

    return s


print(sum_mul(4, 123))

# def sum_mul(n, m):
#     if m > 0 and n > 0:
#         return sum(range(n, m, n))
#     else:
#         return 'INVALID'
