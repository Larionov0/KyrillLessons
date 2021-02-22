def euclid(n1, n2):
    """

    :param n1:
    :param n2:
    :return: int: НОД
    """
    if n1 > n2:
        big = n1
        small = n2
    else:
        small = n1
        big = n2

    ost = big % small
    if ost == 0:
        return small
    else:
        return euclid(small, ost)


print(euclid(125653626, 30))
