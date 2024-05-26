def count_sheep(n):
    sheeps = ''
    for i in range(1, n + 1):
        sheeps += f'{i} sheep...'
    return sheeps


print(count_sheep(3))


# def count_sheep(n):
#     return ''.join(f'{i} sheep...' for i in range(1, n + 1))
