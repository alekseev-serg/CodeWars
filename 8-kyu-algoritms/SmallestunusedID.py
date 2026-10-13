"""
Эй, классный программист!

Вам нужно управлять большим количеством данных, и, конечно же, вы используете нулевые и неотрицательные идентификаторы, 
чтобы сделать каждый элемент данных уникальным!

Поэтому вам нужен метод, который возвращает наименьший неиспользуемый идентификатор для 
вашего следующего нового элемента данных...

Примечание: Указанный массив используемых идентификаторов может быть не отсортирован. 
В целях тестирования могут быть дублирующиеся идентификаторы, но вам не обязательно их находить или удалять!

test.assert_equals(next_id([0,1,2,3,4,5,6,7,8,9,10]), 11, "For input: [0,1,2,3,4,5,6,7,8,9,10]")
test.assert_equals(next_id([5,4,3,2,1]), 0, "For input: [5,4,3,2,1]")
test.assert_equals(next_id([0,1,2,3,5]), 4, "For input: [0,1,2,3,5]")
test.assert_equals(next_id([0,0,0,0,0,0]), 1, "For input: [0,0,0,0,0,0]")
test.assert_equals(next_id([]), 0, "For input: []")
test.assert_equals(next_id([0,0,1,1,2,2]), 3, "For input: [0,0,1,1,2,2]")
test.assert_equals(next_id([0,1,1,1,3,2]), 4, "For input: [0,1,1,1,3,2]")
test.assert_equals(next_id([0,1,0,2,0,3]), 4, "For input: [0,1,0,2,0,3]")
test.assert_equals(next_id([9,8,0,1,7,6]), 2, "For input: [9,8,0,1,7,6]")
test.assert_equals(next_id([9,8,7,6,5,4]), 0, "For input: [9,8,7,6,5,4]")
test.assert_equals(next_id([8,0]), 1, "For input: [8,0]")
"""
def next_id(arr):
    used = set(arr)

    print(used)
    for i in range(len(arr) + 1):
        if i not in used:
            return i
        


print(next_id([0,0,1,1,2,2]))