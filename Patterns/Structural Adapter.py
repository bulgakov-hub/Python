""" Адаптер - структурный паттерн проектирования, который позволяет объектам
с несовместимыми интерфейсами работать вместе.
"""


class Target:
    """ Целевой класс объявляет интерфейс, с которым работает клиентский код
    Нельзя изменять
    """

    def get_value(self) -> str:
        return "2020"


def client_code(target: "Target") -> None:
    """ Клиентский код поддерживает все классы, использующие интерфейс Target
    Нельзя изменять
    """

    print("Выбранное значение: " + target.get_value())


class NewTarget:
    """ Новый класс (Адаптируемый) с которым должен работать c клиентским кодом
    Нельзя изменять
    """

    def get_value(self) -> int:
        return 1980


class AdapterOne(NewTarget, Target):
    """ Адаптер делает интерфейс Адаптируемого класса совместимым с Целевым (Target)
    Через наследование
    """

    def get_value(self) -> str:
        value = super().get_value()
        return str(value)


class AdapterTwo(Target):
    """ Адаптер делает интерфейс Адаптируемого класса совместимым с Целевым (Target)
    Через агрегацию
    """

    def __init__(self, new_target: NewTarget) -> None:
        self.new_target = new_target

    def get_value(self) -> str:
        return str(self.new_target.get_value())


if __name__ == '__main__':
    target = Target()  # Экземпляр класса Target
    client_code(target)  # Используем клиентский код

    # Выбранное значение: 2020

    new_target = NewTarget()
    # При использовании клиентского кода
    # client_code(new_target)
    # Ошибка:
    # TypeError: can only concatenate str (not "int") to str
    # В клиентском коде мы ожидаем str

    adapter = AdapterOne()  # Адаптер через наследование
    client_code(adapter)  # Используем клиентский код

    # Результат:
    # Выбранное значение: 2020
    # Выбранное значение: 1980

    adapter = AdapterTwo(new_target)  # Адаптер через агрегацию
    client_code(adapter)  # Используем клиентский код

    # Результат:
    # Выбранное значение: 2020
    # Выбранное значение: 1980
    # Выбранное значение: 1980
