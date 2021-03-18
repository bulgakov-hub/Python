""" Pydantic
    (pip install pydantic)
"""

from pydantic import BaseModel, ValidationError
from typing import List


class Language(BaseModel):
    """ Вложенная структура данных """

    id: int
    name: str


class Human(BaseModel):
    """ Описание структуры данных """

    id: int
    age: int
    first_name: str
    last_name: str
    languages: List[Language]


# Входящий json
input_json = """ {"id": "1",
          "age": "30 лет",
          "first_name": "Василий",
          "last_name": "Гаврилов",
          "languages": [{"id": 1,
                         "name": "python"},
                        {"id": 2,
                         "name": "golang"},
                        {"id": "id=>3",
                         "name": "java"}]} """

if __name__ == "__main__":

    # Валидация / Вывод ...
    try:
        human = Human.parse_raw(input_json)
    except ValidationError as e:
        print(e.json())
    else:
        print(human)
