""" Алгоритм быстрой сортировки """

from random import randint


def quick_sort(generic_list: list):
    if len(generic_list) < 2:
        return generic_list
    else:
        base_point = generic_list[0]
        minimal = [i for i in generic_list[1:] if i <= base_point]
        maximal = [i for i in generic_list[1:] if i > base_point]

        return quick_sort(minimal) + [base_point] + quick_sort(maximal)


if __name__ == '__main__':

    # Генерируем список из случайных целых значений от 0 до 100
    mylist = [randint(0, 100) for i in range(20)]
    print('Список:', mylist)
    # Список: [95, 18, 19, 0, 77, 43, 36, 44, 71, 54, 16, 41, 13, 4, 46, ...

    print('Отсортированный список:', quick_sort(mylist))
    # Список: [0, 4, 13, 16, 18, 19, 28, 34, 36, 41, 43, 44, 46, ...
