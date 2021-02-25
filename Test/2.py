lst1 = (2, 4, 6, 8, 10, 12, 13, 11, 22)
lst2 = (1, 4, 7, 9, 10, 13, 13, 13, 22)
lst3 = (3, 4, 7, 6, 10, 11, 13, 14, 22)


def match(lst1, lst2, lst3):
    numbers = []
    for i in range(len(lst1)):
        if lst1[i] == lst2[i] == lst3[i]:
            # print(lst1[i], end=" ")
            numbers.append(lst1[i])
    return numbers


match(lst1, lst2, lst3)
