""" Реализация бинарного поиска """

def binary_search(generic_list: list, item: int):
    """ Бинарный поиск элемента в отсортированном списке """

    generic_list.sort()
    min_index = 0 
    max_index = len(generic_list) - 1 
    
    while min_index <= max_index:
        index_middle = (min_index + max_index)
        item_middle = generic_list[index_middle]

        if item_middle == item: 
            return index_middle
        if item_middle > item: 
            max_index = index_middle - 1 
        else:
            min_index = index_middle + 1 

    return None


if __name__ == '__main__':

    mylist = [i for i in range(1,431,3)] # Генерируем список
    print(mylist)
    # [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
    
    item_search = int(input('Введите значение:'))
    print('Индекс найденного элемента в списке:', binary_search(mylist, item_search))
    # Введите значение:13
    # Индекс найденного элемента в списке: 4
    
