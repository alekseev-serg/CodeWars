def grow(arr):
    mult = 1
    for i in arr:
        mult *= i

    return mult


print(grow([1, 2, 3, 4]))
