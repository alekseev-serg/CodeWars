signature = [1, 1, 1]

'0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377'


def tribonacci(signature, n):
    pass


def fibonacci(fib1, fib2, n):
    fib_list = []
    fib_list.append(fib1)
    fib_list.append(fib2)
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        fib_list.append(fib_sum)
        i = i + 1

    return fib_list


print(fibonacci(0, 1, 12))
