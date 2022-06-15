from typing import Dict

from .exception import NoSuchPositionError

POSITIONS: Dict[str, int] = {
    'CEO': 0,
    'manager': 1,
    'developer': 2,
    'tester': 3,
}


def get_position_level(position_name: str) -> int:
    try:
        return POSITIONS[position_name]
    except KeyError as exp:
        raise NoSuchPositionError(position_name) from exp


class Employee:
    name: str
    position: str
    _salary: int

    def __init__(self, name: str, position: str, salary: int):
        if type(name) == str and type(position) == str and type(salary) == int:
            self.name = name
            self.position = position
            self._salary = salary
        else:
            raise ValueError

    def get_salary(self) -> int:
        return self._salary

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Employee):
            raise TypeError
        if not (self.position in POSITIONS and other.position in POSITIONS):
            raise ValueError
        return bool(get_position_level(self.position) == get_position_level(other.position))

    def __str__(self):
        return f'name: {self.name} position: {self.position}'

    def __hash__(self):
        return id(self)


class Developer(Employee):
    language: str
    position: str = 'developer'

    def __init__(self, name: str, salary: int, language: str):
        super().__init__(name, self.position, salary)
        self.language = language


class Manager(Employee):

    position: str = 'manager'

    def __init__(self, name: str, salary: int):
        super().__init__(name, self.position, salary)
