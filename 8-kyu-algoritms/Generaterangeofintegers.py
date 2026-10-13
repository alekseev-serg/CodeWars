"""
Реализуйте функцию generateRange, которая принимает три аргумента (start, stop, step) 
и возвращает диапазон целых чисел от start до stop (включительно) с шагом step.

Примеры
(1, 10, 1) -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
(-10, 1, 1) -> [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1]
(1, 15, 20) -> [1]
Примечание
запуск <
шаг остановки > 0
"""

def generate_range(start, stop, step):
    result = []
    for i in range(start, stop + 1, step):
        result.append(i)
    return result

def generate_range_more(min, max, step):
    return list(range(min, max + 1, step))

print(generate_range(1, 10, 1))      # Вывод: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(generate_range(-10, 1, 1))     # Вывод: [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1]
print(generate_range(1, 15, 20))     # Вывод: [1]