def to_csv_text(array):
    for item in array:
        string_list = [str(s) for s in item]
        print(','.join(string_list), end='\n')


to_csv_text([
    [0, 1, 2, 3, 45],
    [10, 11, 12, 13, 14],
    [20, 21, 22, 23, 24],
    [30, 31, 32, 33, 34]
])
