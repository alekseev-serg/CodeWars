a = ["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]
b = ["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]
c = ["lets", "talk", "about", "javascript", "the", "best", "language"]
d = ["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]
e = ["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]


def two_sort(array):
    array.sort()
    return '***'.join([item for item in array[0]])


print(two_sort(a))
