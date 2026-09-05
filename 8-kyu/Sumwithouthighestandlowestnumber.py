def sum_array(arr):
    if type(arr) != list:
        return 0
    if len(arr) > 1:
        arr.remove(max(arr))
        arr.remove(min(arr))
        return sum(arr)

    if len(arr) <= 1 or type(arr) != list:
        return 0


# { 6, 2, 1, 8, 10 } => 16
# { 1, 1, 11, 2, 3 } => 6

sum_array([6, 2, 1, 8, 10])


# def sum_array(arr):
#     if arr == None or len(arr) < 3:
#         return 0
#     return sum(arr) - max(arr) - min(arr)