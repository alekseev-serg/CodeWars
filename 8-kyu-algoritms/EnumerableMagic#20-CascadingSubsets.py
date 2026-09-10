"""
Создайте метод each_cons, который принимает список и число n и возвращает каскадные подмножества списка размером n,
например:

each_cons([1,2,3,4], 2)
  #=> [[1,2], [2,3], [3,4]]

each_cons([1,2,3,4], 3)
  #=> [[1,2,3],[2,3,4]]

Как видите, списки являются каскадными, то есть они пересекаются, но не нарушен порядок элементов.
"""


def each_cons(list_number, count):
    result = []
    for i in range(len(list_number) - count + 1):
        result.append(list_number[i:i + count])

    return result


print(each_cons([1,2,3,4], 2))