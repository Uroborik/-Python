from functools import reduce


class Order:
    def __init__(self, number, client, cost, status):
        self.number = number
        self.client = client
        self.cost = cost
        self.status = status


orders = [
    Order(1, "Иванов", 1200, "активен"),
    Order(2, "Петров", 800, "отменён"),
    Order(3, "Иванов", 2500, "активен"),
    Order(4, "Сидоров", 1500, "активен"),
    Order(5, "Петров", 600, "отменён"),
]

active = list(filter(lambda o: o.status == "активен", orders))
numbers = list(map(lambda o: o.number, orders))
by_cost = sorted(orders, key=lambda o: o.cost)
total = reduce(lambda s, o: s + o.cost, orders, 0)
has_cancelled = any(o.status == "отменён" for o in orders)


def client_orders(client):
    for o in orders:
        if o.client == client:
            yield o


print("Активные заказы:", [o.number for o in active])
print("Номера всех заказов:", numbers)
print("По возрастанию стоимости:", [o.number for o in by_cost])
print("Общая стоимость:", total)
print("Есть отменённые:", has_cancelled)
print("Заказы Иванова:", [o.number for o in client_orders("Иванов")])
