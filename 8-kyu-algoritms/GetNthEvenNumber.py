"""
Верните N-е четное число

Пример(Ввод --> Вывод)

1 --> 0 (первое четное число — 0)
3 --> 4 (3-е четное число — 4 (0, 2, 4))
100 --> 198
1298734 --> 2597466
Ввод не будет равен 0.
"""


def get_nth_even_number(n):
    count = 0
    num = 0
    while True:
        count += 1
        if count == n:
            return num
        num += 2

def nth_even_number(n):
    return (n - 1) * 2

def main():
    print(get_nth_even_number(100))


if __name__ == '__main__':
    main()
