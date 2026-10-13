"""
Выполните функцию, которая принимает два аргумента и возвращает все числа, которые делятся на заданный делитель. 
Первый аргумент - это массив чисел, а второй - делитель.

Example(Input1, Input2 --> Output)
[1, 2, 3, 4, 5, 6], 2 --> [2, 4, 6]
"""

def divisible_by(numbers, divisor):
    return [item for item in numbers if item % divisor == 0]


print(divisible_by([1, 2, 3, 4, 5, 6], 2))
