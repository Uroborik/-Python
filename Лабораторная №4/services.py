from exceptions import OrderNotFoundError


class OrderService:
    def __init__(self, orders):
        self.orders = orders

    def add(self, order):
        self.orders.append(order)

    def find(self, number):
        for o in self.orders:
            if o.number == number:
                return o
        raise OrderNotFoundError(f"Заказ №{number} не найден")

    def set_status(self, number, status):
        self.find(number).status = status

    def cancel(self, number):
        self.find(number).status = "отменён"
