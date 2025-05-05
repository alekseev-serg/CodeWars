def is_opposite(s1, s2):
    return False if not (s1 or s2) else s1.swapcase() == s2


if __name__ == '__main__':
    print(is_opposite('aB', 'Ab'))
