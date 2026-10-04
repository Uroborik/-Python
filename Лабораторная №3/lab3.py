class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value

    def total_cost(self):
        return self._price

    def get_info(self):
        return f"{self.name}: {self._price} руб."


class Dish(MenuItem):
    def __init__(self, name, price, calories):
        super().__init__(name, price)
        self.calories = calories

    def get_info(self):
        return f"Блюдо {self.name}: {self._price} руб., {self.calories} ккал"


class Drink(MenuItem):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume

    def total_cost(self):
        if self.volume > 500:
            return self._price + 20
        return self._price

    def get_info(self):
        return f"Напиток {self.name}: {self._price} руб., {self.volume} мл"


class Order:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def show(self):
        for item in self.items:
            print(item.get_info())

    def total(self):
        return sum(item.total_cost() for item in self.items)


order = Order()
order.add(Dish("Борщ", 250, 320))
order.add(Dish("Стейк", 700, 650))
order.add(Drink("Сок", 120, 300))
order.add(Drink("Морс", 150, 1000))
order.show()
print("Итого:", order.total(), "руб.")