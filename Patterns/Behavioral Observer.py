""" Наблюдатель - это поведенческий паттерн, который позволяет объектам оповещать
другие объекты об изменениях своего состояния.
"""


from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Интерфейс Наблюдателя объявляет метод уведомления, которые издатели
    используют для оповещения своих подписчиков.
    """

    @abstractmethod
    def update(self, msg: str) -> None:
        """ Получение нового сообщения 
        """
        pass


class People(Observer):
    """ Наблюдатель человек из РФ читающий местные газетки
    """

    def __init__(self, name: str) -> None:
        """ Конструктор, добавляем Имя человека
        """ 
        self.name = name

    def update(self, msg: str) -> None:
        """ Получение новости из газетки
        """
        print(f'{self.name} Узнал из газеты что: {msg}')
        

class Observable(ABC):
    """ Абстрактный класс наблюдаемого (за кем наблюдают)
    """

    def __init__(self) -> None:
        """ Конструктор, инициализируем список наблюдателей
        """
        self.observers = []

    def register(self, observer: Observer) -> None:
        """ Регистрация нового наблюдателя на подписку,
            добавляем в список
        """
        self.observers.append(observer)

    def notify_observers(self, msg: str) -> None:
        """ Передача сообщения всем наблюдателям, подписанным на события
            данного объекта наблюдаемого класса
        """
        print('Уважаемые подписчики, Внимание! последние новости!')
        for observer in self.observers:
            observer.update(msg)


class Newspaper(Observable):
    """ Газета Россия24, за новостями в которой следят тысячи людей
    """

    def add_news(self, news: str) -> None:
        """ Выпуск очередной новости
        """
        self.notify_observers(news)


if __name__ == '__main__':

    # Создаем Газету
    newspaper = Newspaper()

    # Подписываем товарщией на новости
    newspaper.register(People('Виктор Сергеевич'))
    newspaper.register(People('Азамат Азаматович'))
    newspaper.register(People('Алексей Петрович'))

    # Создаем новость
    newspaper.add_news('Путин поднял пенсионные возраст всем до 95 лет')
    newspaper.add_news('Путин всем выплатил компенсацию в размере 1000 рублей')
    
