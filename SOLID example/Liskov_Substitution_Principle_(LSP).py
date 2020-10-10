""" Liskov Substitution Principle (LSP) - принцип подстановки Барбары Лисков
Интерпритация Р.Мартина: Функции, которые используют базовый тип, должны
использовать подтипы базового типа, не зная об этом
Наследующий класс должен дополнять, а не замещать поведение базового класса.
"""


class Vehicle:
    """ Транспортное средство """

    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self) -> str:
        return f'Название транспортного средства: {self.name}'

    def get_speed(self) -> str:
        return f'Скорость транспортного средства: {self.speed}'


class VehicleWithoutMotor(Vehicle):
    """ Транспортное средство без мотора """

    def start_moving(self):
        pass


class VehicleWithMotor(Vehicle):
    """ Транспортное средство с мотором """

    def start_engine(self):
        pass


class Car(VehicleWithMotor):
    """ Класс Автомобиль """

    def start_engine(self):
        print(f'Завел двигатель "{self.name}" и поехал {self.speed}')


class Bicycle(VehicleWithoutMotor):
    """ Класс Велосипед """

    def start_moving(self):
        print(f'Велосипед "{self.name}" {self.speed}',
               'Кручу кручу педали кручу ...')


if __name__ == '__main__':
    my_car = Car('Toyota Camry', '120км/ч')
    my_car.start_engine()
    my_bicycle = Bicycle('Салют', '8 км/ч')
    my_bicycle.start_moving()

# Завел двигатель "Toyota Camry" и поехал 120км/ч
# Велосипед "Салют" 8 км/ч Кручу кручу педали кручу ...
