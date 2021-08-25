""" Декоратор - структурный паттерн проектирования, предназначенный для
    динамического подключения дополнительного поведения к объекту.
    Альтернатива создания подклассов с целью расширения функционала.
"""

from abc import ABC, abstractmethod


class Component(ABC):
    """ Базовый интерфейс для Компонента определяет
        поведение, которое изменяется декораторами.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


class MyString(Component):
    """ Реализация компонента """

    def operation(self) -> str:
        return "Hello World!"


class Decorator(Component):
    """ Базовый класс Декоратора следует тому же интерфейсу, что и другие
        компоненты. Основная цель этого класса - определить интерфейс обёртки для
        всех конкретных декораторов.
    """

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component
    
    @property
    def component(self) -> str:
        """ Декоратор делегирует всю работу обёрнутому компоненту.
        """

        return self._component

    def operation(self) -> str:
        return self._component.operation()


class MyDecoratorA(Decorator):
    """ Декоратор вызывает обёрнутый объект и изменяют его результат
        некоторым образом.
    """

    def operation(self) -> str:
        """ Декораторы могут вызывать родительскую реализацию операции, вместо того,
        чтобы вызвать обёрнутый объект напрямую. Такой подход упрощает
        расширение классов декораторов.
        """

        return f"MyDecoratorA({self.component.operation()})"


class MyDecoratorB(Decorator):
    """ Декоратор вызывает обёрнутый объект и изменяют его результат
        некоторым образом.
    """

    def operation(self) -> str:
        """ Декораторы могут вызывать родительскую реализацию операции, вместо того,
        чтобы вызвать обёрнутый объект напрямую. Такой подход упрощает
        расширение классов декораторов.
        """

        return f"MyDecoratorB({self.component.operation()})"


if __name__ == '__main__':
    
    string_component = MyString()
    print('без декоратора', string_component.operation())

    decoratorA = MyDecoratorA(string_component)
    print('декоратор А:', decoratorA.operation())

    decoratorB = MyDecoratorB(decoratorA)
    print('декоратор B:', decoratorB.operation()) 
