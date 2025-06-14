# ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]), [10, -65])
# ([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]), [8, -50])
# ([1]), [1, 0])
# ([-1]), [0, -1])
# ([0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 0])
# ([]), [])
def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    else:
        count = 0
        mult = 0
        for i in range(len(arr)):
            if arr[i] > 0:
                count += 1
            if arr[i] < 0:
                mult += arr[i]
        return [count, mult]


print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
