from abc import ABC, abstractmethod


class Subscription:
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price


class SubscriptionFactory:
    prices = {"разовый": 300, "месячный": 2000, "годовой": 18000}

    @staticmethod
    def create(kind):
        if kind not in SubscriptionFactory.prices:
            raise ValueError("Неизвестный тип абонемента")
        return Subscription(kind, SubscriptionFactory.prices[kind])


class PricingStrategy(ABC):
    @abstractmethod
    def price(self, base):
        ...


class StandardStrategy(PricingStrategy):
    def price(self, base):
        return base


class DiscountStrategy(PricingStrategy):
    def price(self, base):
        return base * 0.9


class FamilyStrategy(PricingStrategy):
    def price(self, base):
        return base * 2 * 0.8


class Observer(ABC):
    @abstractmethod
    def update(self, event):
        ...


class Logger(Observer):
    def update(self, event):
        print(f"[LOG] {event}")


class Notification(Observer):
    def update(self, event):
        print(f"[СМС] {event}")


class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, event):
        for o in self.observers:
            o.update(event)


class SubscriptionRepository:
    def __init__(self):
        self.items = []

    def add(self, subscription):
        self.items.append(subscription)

    def count(self):
        return len(self.items)


class FitnessService(Subject):
    def __init__(self, strategy, repository):
        super().__init__()
        self.strategy = strategy
        self.repository = repository

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sell(self, kind):
        subscription = SubscriptionFactory.create(kind)
        price = self.strategy.price(subscription.base_price)
        self.repository.add(subscription)
        self.notify(f"Продан абонемент '{kind}' за {price} руб.")
        return price


def test_factory():
    sub = SubscriptionFactory.create("месячный")
    assert sub.base_price == 2000


def test_strategy():
    base = 1000
    assert DiscountStrategy().price(base) < StandardStrategy().price(base)


def test_repository():
    repo = SubscriptionRepository()
    repo.add(SubscriptionFactory.create("разовый"))
    assert repo.count() == 1


def test_sell():
    service = FitnessService(DiscountStrategy(), SubscriptionRepository())
    assert service.sell("годовой") == 18000 * 0.9


def test_observer():
    received = []

    class Spy(Observer):
        def update(self, event):
            received.append(event)

    service = FitnessService(StandardStrategy(), SubscriptionRepository())
    service.subscribe(Spy())
    service.sell("разовый")
    assert len(received) == 1


def run_tests():
    for test in [test_factory, test_strategy, test_repository, test_sell, test_observer]:
        test()
        print(f"{test.__name__}: OK")


repo = SubscriptionRepository()
service = FitnessService(StandardStrategy(), repo)
service.subscribe(Logger())
service.subscribe(Notification())

print("Стандарт:", service.sell("месячный"), "руб.")
service.set_strategy(DiscountStrategy())
print("Скидка:", service.sell("месячный"), "руб.")
service.set_strategy(FamilyStrategy())
print("Семейный:", service.sell("годовой"), "руб.")
print("Продано абонементов:", repo.count())

print("--- Тесты ---")
run_tests()
