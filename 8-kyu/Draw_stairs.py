def draw_stairs(n):
    return '\n'.join(' '*i+'I' for i in range(n))


def draw_stairs_another(n):
    s = ""
    for i in range(1, n + 1):
        s += 'I\n' + ' ' * i
    return s.strip()
