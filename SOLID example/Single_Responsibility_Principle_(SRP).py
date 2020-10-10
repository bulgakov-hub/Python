""" Single Responsibility Principle (SRP) - Принцип единой ответственности
Модуль (класс) должен иметь одну и только одну причину для изменения.
Каждый объект должен иметь одну ответственность и эта ответственность должна
быть полностью инкапсулирована в класс. Все его поведения должны быть
направлены на обеспечение этой ответственности.
Недостатки: SRP может привести к обилию мелких классов/методов и
размазыванию логики между ними.
"""

from dataclasses import dataclass


class Connection:
    """ Connection """

    def open(self):
        print('Открыть соединение к БД')

    def exec(self, sql):
        print(f'Исполняется SQL запрос на сохранение данных в БД: {sql}')

    def close(self):
        print('Закрываем соединение к БД')


"""
Класс у которого много причин для изменения, необходимо изменить:
class UserView:
    def post(self, *args, **kwargs):
        name = kwargs.get('name')
        age = kwargs.get('age')
        if not name or not age:
            raise Exception('Необходимо заполнить все поля')
        if not isinstance(age, int):
            raise Exception('Возраст должен быть целым')
        connection = Connection()
        connection.open()
        connection.exec(
            f'INSERT INTO users (name, age) values ({name}, {age})'
            )
        connection.close()
        return 'HTTP/1.1 200 OK Content-Type: text/html'
"""


@dataclass
class User:
    """ User """

    name: str
    age: str


class UserRepository:
    """ UserRepository """

    table = 'user'
    insert_sql = 'INSERT INTO users (name, age) values ({name}, {age})'
    connection = Connection()

    def insert(self, user: User):
        self.connection.open()
        self.connection.exec(self.insert_sql.format(
            name=user.name,
            age=user.age))
        self.connection.close()


class UserSerializer:
    """ Serializer """

    model = User

    def __init__(self, data: dict):
        self.data = data

    def validate(self):
        name = self.data.get('name')
        age = self.data.get('age')
        if not name or not age:
            raise Exception('Необходимо заполнить все поля')
        if not isinstance(age, int):
            raise Exception('Возраст должен быть целым числом')
        return User(name, age)


class HttpResponse:
    """ HttpResponse """

    def __init__(self, code='200 OK', content_type='text/html'):
        self.code = code
        self.content_type = content_type

    def to_string(self):
        return f'HTTP/1.1 {self.code} Content-Type: {self.content_type}'


class UserView:
    """ Класс контроллер """

    serializer_class = UserSerializer
    repository_class = UserRepository
    response_class = HttpResponse

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(kwargs)
        user = serializer.validate()
        repository = self.repository_class()
        repository.insert(user)

        return self.response_class().to_string()

if __name__ == '__main__':
    view = UserView()
    response = view.post(name='Василий Петрович', age=19)
    print(response)

# Открыть соединение к БД
# Исполняется SQL запрос на сохранение данных в БД:
# INSERT INTO users (name, age) values (Василий Петрович, 21)
# Закрываем соединение к БД
# HTTP/1.1 200 OK Content-Type: text/html
