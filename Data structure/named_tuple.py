from pympler import asizeof
import random
from random import choice
from string import ascii_lowercase
from typing import NamedTuple


def size_byte(num, suffix='B'):
    """ Указываем размер в байтах """

    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


list_dicts = []
for i in range(1000):
    list_dicts.append({
        'name': ''.join([choice(ascii_lowercase) for _ in range(100)]),
        'options': [{
            'set_1': 9223372036854775807,
            'set_2': 9223372036854775807,
            'set_3': 9223372036854775807,
        } for _ in range(30)] 
    })

print(f'Размер List[Dict] в памяти составляет:' 
    f'{size_byte(asizeof.asizeof(list_dicts))}'
)


class OptionsTuple(NamedTuple):
    set_1: int
    set_2: int
    set_3: int


tuple_dicts = []
for i in range(1000):
    tuple_dicts.append({
        'name': ''.join([choice(ascii_lowercase) for _ in range(100)]),
        'options': [
            OptionsTuple(
                set_1=9223372036854775807,
                set_2=9223372036854775807,
                set_3=9223372036854775807,
            ) for _ in range(30)] 
    })

print(f'Размер List[namedtuple] в памяти составляет:' 
    f'{size_byte(asizeof.asizeof(tuple_dicts))}'
)

# Размер List[Dict] в памяти составляет:7.3MB
# Размер List[namedtuple] в памяти составляет:2.5MB