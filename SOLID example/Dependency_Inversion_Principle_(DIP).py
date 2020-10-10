""" Dependency Inversion Principle (DIP) — Принцип инверсии зависимости.
Cвязь между классами должна осуществляться через интерфейс.
Это позволит при необходимости заменить конкретную реализацию интерфейса
на другую, без необходимости внесения изменений в основной код.
Недостатки: Интерфейсы выделяются для каждого класса и пачками передаются
через конструкторы. Понять, где находится логика становится практически
невозможно.
"""

from abc import ABC, abstractmethod


class Mail(ABC):
    """ Интерфейс класса нижнего уровня для провайдеров сообщений """

    @abstractmethod
    def send_message(self, email, message):
        pass


class Gmail(Mail):
    """ Класс нижнего уровня: Отправка сообщений через Gmail """

    def send_message(self, email, message):
        print(f'Gmail: отправляю сообщение "{message}" на адрес {email}')


class Yandex(Mail):
    """ Класс нижнего уровня: Отправка сообщений через Gmail """

    def send_message(self, email, message):
        print(f'Yandex: отправляю сообщение "{message}" на адрес {email}')


class Notification():
    """ Класс верхнего уровня: Уведомление, зависит от абстракции Mail """

    def __init__(self, mail: Mail):
        self.mail = mail

    def notify(self, email, message):
        self.mail.send_message(email, message)

if __name__ == '__main__':
    mailing = Notification(Gmail())
    mailing.notify('test@test.ru', 'Notification!')
    mailing = Notification(Yandex())
    mailing.notify('test@test.ru', 'Notification!')

# Gmail: отправляю сообщение "Notification!" на адрес test@test.ru
# Yandex: отправляю сообщение "Notification!" на адрес test@test.ru
