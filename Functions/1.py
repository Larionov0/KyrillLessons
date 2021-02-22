def printer(name):
    print('Hello', name, '!')


def summer(numbers):
    """
    :param numbers: [1, 5, 2, 6]
    :return: 14
    """
    result = 0
    for number in numbers:
        result += number
    return result


numbers = [1, 6, 3, 8, 5]
s = summer(numbers)

if s >= 20:
    print(':)')
else:
    print(":(")
