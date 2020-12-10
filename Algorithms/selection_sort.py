""" Сортировка выбором (selection sort) """

from random import randint


def find_small(generic_list: list):
    """ Поиск индекса наименьшего значения в списке """

    small = generic_list[0]
    small_index = 0

    for i in range(1, len(generic_list)):
        if generic_list[i] < small:
            small = generic_list[i]
            small_index = i

    return small_index


def selection_sort(generic_list: list):
    """ Функция сортировки выбором """

    sorted_list = []
    for i in range(len(generic_list)):
        small_index = find_small(generic_list)
        sorted_list.append(generic_list.pop(small_index))

    return sorted_list


def selection_sort2(generic_list: list):
    """ Функция сортировки выбором """

    for i, e in enumerate(generic_list):
        small_index = min(range(i, len(generic_list)),
                          key=generic_list.__getitem__)
        generic_list[i], generic_list[small_index] = generic_list[small_index], e

    return generic_list


if __name__ == '__main__':

    # Генерируем список из случайных целых значений от 0 до 100
    mylist = [randint(0, 100) for i in range(20)]
    print('Список:', mylist)
    # Список: [27, 60, 13, 5, 75, 71, 85, 26, 96, 37, 70, 41, 51, 17 ..

    # Сортировка выбором
    mylist_sort = selection_sort(mylist)
    print('Отсортированный список:', mylist_sort)
    # Отсортированный список: [1, 4, 4, 4, 5, 5, 5, 7, 8, 8, 9, 11, ..

    mylist2 = [randint(0, 100) for i in range(20)]
    print('Список:', mylist2)

    mylist2_sort = selection_sort2(mylist2)
    print('Отсортированный список:', mylist2_sort)
