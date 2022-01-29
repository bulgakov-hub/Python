""" Рекурсивный алгоритм бинарного поиска """

if __name__ == '__main__':

    mylist = [i for i in range(1, 431, 3)] # Генерируем список
    print(mylist)

    item_search = int(input('Введите значение:'))

    # Lambda функция
    binary_search = lambda mylist, item_search, lo, hi: -1 if lo>hi else \
                    (lo+hi)//2 if mylist[(lo+hi)//2] == item_search else \
                    binary_search(mylist, item_search, lo, (lo+hi)//2-1) if mylist[(lo+hi)//2] > item_search else \
                    binary_search(mylist, item_search, (lo+hi)//2+1, hi)
    # Результат
    print('Индекс найденного элемента в списке:',
           binary_search(mylist, item_search, 0, len(mylist)-1))
