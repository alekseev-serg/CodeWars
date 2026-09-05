def multi_table(number):
    lines = []
    for i in range(1, 11):
        lines.append(f'{i} * {number} = {i * number}')
    return '\n'.join(lines)


print(multi_table(5))


# def multi_table(number):
#     return "\n".join(f"{i} * {number} = {i * number}" for i in range(1, 11))