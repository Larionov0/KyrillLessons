"""
Необходимо отсортировать первые две трети списка в порядке возрастания,
если среднее арифметическое всех элементов больше нуля;
иначе — лишь первую треть.
Остальную часть списка не сортировать, а расположить в обратном порядке
"""


def bubble_sort(myList):
    swapped = True
    ogr = len(myList) - 1
    while swapped:
        swapped = False  # никакого обмена местами
        for i in range(ogr):
            if myList[i] > myList[i + 1]:
                swapped = True  # произошёл обмен местами!
                myList[i], myList[i + 1] = myList[i + 1], myList[i]
        ogr -= 1


def sort_2_3(lst):
    ser = sum(lst) / len(lst)
    if ser > 0:
        last_index = len(lst) * 2 // 3
    else:
        last_index = - (len(lst) * 2 // 3)
    left_part = lst[:last_index]
    bubble_sort(left_part)
    right_part = lst[last_index:]
    right_part.reverse()
    return left_part + right_part
