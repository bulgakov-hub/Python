from abc import ABC, abstractmethod

""" Interface Segregation Principle (ISP) - принцип разделения интерфейсов.
Клиенты не должны зависеть от методов, которые они не используют.
Недостатки: Принцип тысячи интерфейсов. Интерфейсы классов разбиваются на
слишком большое число составляющих, что делает их неудобными для использования
всеми клиентами.
"""


class NotifyBySms(ABC):
    """ Интерфейс уведомления по смс """

    @property
    @abstractmethod
    def phone(self):
        pass

    @abstractmethod
    def notify_by_sms(self):
        pass


class NotifyByEmail(ABC):
    """ Интерфейс уведомления по почте """

    @property
    @abstractmethod
    def email(self):
        pass

    @abstractmethod
    def notify_by_email(self):
        pass


class NotifyByFax(ABC):
    """ Интерфейс уведомления по факсу """

    @property
    @abstractmethod
    def fax(self):
        pass

    @abstractmethod
    def notify_by_fax(self):
        pass


class ExpertUser(NotifyBySms, NotifyByFax):
    """ Уведомления Expert пользователя """

    def __init__(self, phone, fax):
        self._phone = phone
        self._fax = fax

    @property
    def phone(self):
        return self._phone

    @property
    def fax(self):
        return self._fax

    def notify_by_sms(self):
        print(f'Уведомление пользователя Expert по sms:{self._phone}')

    def notify_by_fax(self):
        print(f'Уведомление пользователя Expert по fax:{self._fax}')


class InternetUser(NotifyByEmail):
    """ Уведомление Internet пользователя """

    def __init__(self, email):
        self._email = email

    @property
    def email(self):
        return self._email

    def notify_by_email(self):
        print(f'Уведомление пользователя Expert по email:{self._email}')


if __name__ == '__main__':
    expert_user = ExpertUser('+7123456789', '22-33-55')
    expert_user.notify_by_sms()
    expert_user.notify_by_fax()
    internet_user = InternetUser('test@test.ru')
    internet_user.notify_by_email()

# Уведомление пользователя Expert по sms номер:+7123456789
# Уведомление пользователя Expert по fax номер:22-33-55
# Уведомление пользователя Expert по email почта:test@test.ru
