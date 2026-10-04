import time
from dataclasses import dataclass
from enum import Enum
from functools import wraps
from contextlib import contextmanager
from typing import Protocol


class Status(Enum):
    ACTIVE = "активен"
    EXPIRED = "истёк"
    FROZEN = "заморожен"
    CANCELLED = "отменён"


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] вызван {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"[PERF] {func.__name__}: {time.perf_counter() - start:.6f} sec")
        return result
    return wrapper


def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


class Reportable(Protocol):
    def report(self) -> str:
        ...


@dataclass
class Person:
    name: str

    def report(self) -> str:
        return self.name


@dataclass
class Client(Person):
    visits: int = 0
    status: Status = Status.ACTIVE

    @log
    def visit(self):
        self.visits += 1

    def report(self) -> str:
        return f"Клиент {self.name}: посещений {self.visits}, абонемент {self.status.value}"


@dataclass
class Trainer(Person):
    specialty: str = "фитнес"

    def report(self) -> str:
        return f"Тренер {self.name}: специализация {self.specialty}"


@dataclass
class Subscription:
    price: int
    months: int
    status: Status = Status.ACTIVE

    def cost(self) -> int:
        return self.price * self.months


@contextmanager
def session(name):
    print(f"[НАЧАЛО] {name}")
    yield
    print(f"[КОНЕЦ] {name}")


@repeat(3)
def add_visit(client: Client):
    client.visit()


@timer
def statistics(clients):
    total = sum(c.visits for c in clients)
    return total / len(clients)


def inspect_object(obj):
    print("Тип:", type(obj).__name__)
    print("Класс:", obj.__class__.__name__)
    print("Атрибуты:", list(vars(obj).keys()))
    print("Есть метод report:", hasattr(obj, "report"))


def show(item: Reportable):
    print(item.report())


client = Client("Иван")
trainer = Trainer("Пётр", "бокс")
sub = Subscription(1500, 3)

with session("тренировки клиента"):
    add_visit(client)

show(client)
show(trainer)
print("Стоимость абонемента:", sub.cost(), "руб.")
print("Средняя посещаемость:", statistics([client]))
inspect_object(client)
