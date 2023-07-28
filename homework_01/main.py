"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    square = []
    for arg in args:
        square.append(arg ** 2)
    return square


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    """
    функция, которая проверяет является ли число простым,
    возвращает True или False
    """
    if number in (0, 1):
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
    return True


def filter_numbers(*args):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if args[1] == "odd":
        return [number for number in args[0] if number % 2 != 0]
    elif args[1] == "even":
        return [number for number in args[0] if number % 2 == 0]
    elif args[1] == "prime":
        return list(filter(is_prime, args[0]))
