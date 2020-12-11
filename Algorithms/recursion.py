""" Рекурсия - это способ задания алгоритма вычисления функции
с использованием вызова ею самой себя
"""


def countdown(i):
    """ Примерчик """

    print(i, end=', ')
    if i <= 0:  # Базовый случай
        return print(end='\n')
    else:  # Рекурсивный случай
        countdown(i - 1)  # Рекурсивный вызов


def factorial(n: int):
    """ Факториал числа """

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n: int) -> list:
    """ Числа Фибоначчи """

    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    fib_list = fibonacci(n - 1)
    fib_list.append(fib_list[-1] + fib_list[-2])

    return fib_list


def fib(n: int) -> int:
    """ Число Фибоначчи """
    
    return fib(n - 1) + fib(n - 2) if n > 2 else 1


if __name__ == '__main__':

    countdown(30)
    # 30, 29, 28, 27, 26, 25, 24, ...

    print(f'Факториал 5 = {factorial(5)}')
    print(f'Факториал 10 = {factorial(10)}')
    # Факториал 5 = 120
    # Факториал 10 = 3628800

    print('Cписок чисел Фибоначчи:', fibonacci(20))
    # Числа Фибоначчи: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    print('10 число последовательности Фибоначчи:', fib(10))
    # 10 число последовательности Фибоначчи: 55
