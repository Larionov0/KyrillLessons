def _factorial(n): # рекурсивная функция
    """
    5! = 5 * 4 * 3 * 2 * 1 = 120
    f(5) = 120
    f(5) = 5 * f(4) = 5 * 4 * f(3)  = ... 5 * 4 * 3 * 2 * 1 !stop
    f(n) = n * f(n - 1)
    :return:
    """
    if n == 1:
        return 1

    return n * _factorial(n - 1)


def factorial(n):  # обертка
    if n < 0:
        raise ValueError('Меньше 1')
    elif n == 0:
        return 1

    return _factorial(n)


print(factorial(5))
