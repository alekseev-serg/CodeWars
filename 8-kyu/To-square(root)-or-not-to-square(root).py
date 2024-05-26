def square_or_square_root(arr):
    result = []
    for item in arr:
        if str(item ** 0.5)[-1] == '0':
            result.append(int(item ** 0.5))
        else:
            result.append(item * item)

    return result


arr = [4, 3, 9, 7, 2, 1]

print(square_or_square_root(arr))