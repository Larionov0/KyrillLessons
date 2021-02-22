"""
Написать программу «справочник».
Создать два списка целых. Один список хранит идентификационные коды, второй — телефонные номера.
Реализовать меню для пользователя:
■ Отсортировать по идентификационным кодам;
■ Отсортировать по номерам телефона;
■ Вывести список пользователей с кодами и телефонами;
■ Выход.
"""


def parallel_sort(main_list, sub_list):
    swapped = True
    ogr = len(main_list) - 1
    while swapped:
        swapped = False  # никакого обмена местами
        for i in range(ogr):
            if main_list[i] > main_list[i + 1]:
                swapped = True  # произошёл обмен местами!
                main_list[i], main_list[i + 1] = main_list[i + 1], main_list[i]
                sub_list[i], sub_list[i + 1] = sub_list[i + 1], sub_list[i]
        ogr -= 1


def point1(ids, phones):
    parallel_sort(ids, phones)


def point2(ids, phones):
    parallel_sort(phones, ids)


def point3(ids, phones):
    """
    ■ Вывести список пользователей с кодами и телефонами
    """
    print('\nДанные:')
    for id, phone in zip(ids, phones):
        print(f"{id} - {phone}")


def main_menu(ids, phones):
    while True:
        text = '--= Главное меню =--\n' \
               '1 - Отсортировать по идентификационным кодам\n' \
               '2 - Отсортировать по номерам телефона\n' \
               '3 - Вывести список пользователей с кодами и телефонами\n' \
               '4 - Выход'
        print(text)
        choice = input('Ваш выбор: ')
        if choice == '1':
            point1(ids, phones)
        elif choice == '2':
            point2(ids, phones)
        elif choice == '3':
            point3(ids, phones)
        elif choice == '4':
            break
        else:
            pass

        print('\n\n\n')


def main():
    ids = [12, 54, 21, 43, 23, 13, 52, 22]
    phones = [121452, 124534, 15364, 532463, 143524, 542124, 423542, 12435]
    main_menu(ids, phones)


main()
