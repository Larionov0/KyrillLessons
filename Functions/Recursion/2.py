def list_numbers_counter(value):
    """
    f([[1], 3, [[2, 1], 5]]) = f([1]) + f([3, [[2, 1], 5]]) =|
    ~ f([1]) = f(1) + f([]) = 1 + 0 = 1
    |= 1 + f([3, [[2, 1], 5]]) = 1 + f(3) + f([[[2, 1], 5]]) =
    = 1 + 3 + f([[[2, 1], 5]]) = 1 + 3 + f([[2, 1], 5]) + f([]) =
    = 1 + 3 + f([[2, 1], 5]) + 0 = 1 + 3 + f([2, 1]) + f([5]) + 0 =
    = 1 + 3 + f(2) + f([1]) + f(5) + f([]) =
    = 1 + 3 + 2 + f([1]) + 5 + 0 =
    = 1 + 3 + 2 + f(1) + f([]) + 5 + 0 =
    = 1 + 3 + 2 + 1 + 0 + 5 + 0 = 12

    :param lst:
    [1, 3, 5, 2, 6]
    [1, [3, 2], 2]
    [[1, 2, [5, 6, [1]], 2, [2, 5, [2, 2, [1, 3]]]], [2, 5, [2, [[[3, [[3]]]]]]]]
    :return: int: sum of numbers
    """
    if isinstance(value, int):
        return value
    elif isinstance(value, list):
        if len(value) == 0:
            return 0

        first_element = value[0]
        list_part = value[1:]
        return list_numbers_counter(first_element) + list_numbers_counter(list_part)
    else:
        raise TypeError('Что ж вы передаете не инты и не листы')


lst = [[1, 2, [5, 6, [1]], 2, [2, 5, [2, 2, [1, 3]]]], [2, [[[[[[[[[1]]]]]]]]], 5, [2, [[[3, [[3]]]]]]]]
print(list_numbers_counter(lst))
