def well(x):
    c = x.count('good')
    return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'


print(well(x=['good', 'bad', 'good', 'bad', 'good', 'bad']))
