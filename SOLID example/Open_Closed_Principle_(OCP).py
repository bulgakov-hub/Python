""" Open Closed Principle (OCP) — Принцип открытости/закрытости
классы должны быть открыты для расширения (для добавления нового функционала)
и закрыты для изменения (изменения кода существующих классов). Делается при
помощи наследования интерфейсов или абстрактных классов.
Интерфейс – класс, где все методы абстрактные;
Абстрактный класс – интерфейс с предопределенной базовой реализацией одного
или нескольких методов;
Можно добавить класс кредитной карты (открыты для расширения), без изменения
абстрактного класса кредитной карты (закрыты для изменения)
"""

from abc import ABC, abstractmethod


class CreditCard(ABC):
    """ Абстрактный класс кредитной карты """

    def __init__(self, code, expiration_date, monthly_const):
        self.code = code
        self.expiration_date = expiration_date
        self.monthly_const = monthly_const

    @abstractmethod
    def get_price_width_discount(self, price):
        pass

    @property
    @abstractmethod
    def discount(self):
        pass


class GoldCreditCard(CreditCard):
    """ Кредитная карта Gold """

    def get_price_width_discount(self, price):
        return self.discount * price

    @property
    def discount(self):
        return 0.9

    def __str__(self):
        return 'Card Gold'


class SilverCreditCard(CreditCard):
    """ Кредитная карта Silver """

    def get_price_width_discount(self, price):
        return self.discount * price

    @property
    def discount(self):
        return 0.9

    def __str__(self):
        return 'Card Silver'


class PlatinumCreditCard(CreditCard):
    """ Кредитная карта Platinum """

    def get_price_width_discount(self, price):
        return self.discount * price

    @property
    def discount(self):
        return 0.99

    def __str__(self):
        return 'Card Platinum'


class TestView:
    """ Test View """

    __card_list = [GoldCreditCard, SilverCreditCard, PlatinumCreditCard]

    def __init__(self, number: str, date: str, price: int):
        self._number = number
        self._date = date
        self._price = price

    @property
    def discount_all_info(self):
        message_list = []
        for card in self.__card_list:
            item = card(self._number, self._date, self._price)
            discount = item.get_price_width_discount(self._price)
            message = (
                "Стоимость товара {} $ со скидкой по карте {} \n"
                "({}, '{}'), составит {} $").format(
                    self._price, item,
                    self._number, self._date, discount)
            message_list.append(message)

        return message_list


if __name__ == '__main__':

    test = TestView('123-123-123', '12/24', 1000)
    for message in test.discount_all_info:
        print(message)

# Стоимость товара 1000 $ со скидкой по карте 'Card Gold'
# (123-123-123, '12/24'), составит 900.0 $
# Стоимость товара 1000 $ со скидкой по карте 'Card Silver'
# (123-123-123, '12/24'), составит 900.0 $
# Стоимость товара 1000 $ со скидкой по карте 'Card Platinum'
# (123-123-123, '12/24'), составит 990.0 $

