def fake_bin(x):
    return ''.join(str(i) for i in [0 if int(item) < 5 else 1 for item in x])


# def fake_bin(x):
#     return ''.join('0' if c < '5' else '1' for c in x)
