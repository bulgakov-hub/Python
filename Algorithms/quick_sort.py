""" Алгоритм быстрой сортировки """

import cProfile
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
    mylist = [randint(0, 1000) for i in range(2000)]
    print('Список:', mylist)
        # Список: [95, 18, 19, 0, 77, 43, 36, 44, 71, 54, 16, 41, 13, 4, 46, ...
    
    print('Отсоротированный список:', quick_sort(mylist))
        # Отсортированный список: [0, 4, 13, 16, 18, 19, 28, 34, 36, 41, 43, 44, 46, ...
    
    cProfile.run('quick_sort(mylist)')
        # 8501 function calls (5669 primitive calls) in 0.014 seconds ...