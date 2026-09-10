"""
Дополните решение так, чтобы оно меняло порядок слов в переданной строке на обратный.

Слова разделяются ровно одним пробелом, начальные и конечные пробелы отсутствуют.

Пример (ввод --> вывод):

"The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"

"""

def reverse_words(s):
    tmp = (s.split(" "))[::-1]
    return " ".join(tmp)

print(reverse_words("The greatest victory is that which requires no battle"))