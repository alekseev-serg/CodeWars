"""
Given 2 elevators (named "left" and "right") in a building with 3 floors (numbered 0 to 2), 
write a function accepting 3 arguments (in order):

left - The current floor of the left elevator
right - The current floor of the right elevator
call - The floor that called an elevator
It should return the name of the elevator closest to the called floor ("left"/"right").

In the case where both elevators are equally distant from the called floor, choose the elevator to the right.

You can assume that the inputs will always be valid integers between 0-2.

Examples:

left right call   result
  0    1     0    "left"
  0    1     1    "right"
  0    1     2    "right"
  0    0     0    "right"
  0    2     1    "right"
"""

def elevator(left, right, call):
    """
    Определяет, какой лифт ближе к вызванному этажу.

    Args:
        left: текущий этаж левого лифта (0-2)
        right: текущий этаж правого лифта (0-2)
        call: этаж, с которого вызвали лифт (0-2)

    Returns:
        str: "left" или "right"
    """

    distance_left = abs(left - call)
    distance_right = abs(right - call)

    if distance_right <= distance_left:
        return "right"
    else:
        return "left"

print(elevator(0,1,0))
print(elevator(0,1,1))
print(elevator(0,1,2))
print(elevator(0,0,0))
print(elevator(0,2,1))
print(elevator(1,1,0))


# Давай напишем тесты для функции elevator, чтобы убедиться, что она работает корректно.
def test_elevator():
    assert elevator(0, 1, 0) == "left"
    assert elevator(0, 1, 1) == "right"
    assert elevator(0, 1, 2) == "right"
    assert elevator(0, 0, 0) == "right"
    assert elevator(0, 2, 1) == "right"
    assert elevator(1, 1, 0) == "right"
    assert elevator(2, 0, 1) == "right"
    assert elevator(2, 2, 2) == "right"
    assert elevator(1, 0, 1) == "left"
    assert elevator(1, 2, 1) == "left"

# Запускаем тесты
test_elevator()
