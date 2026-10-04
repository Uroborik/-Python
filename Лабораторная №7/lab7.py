from abc import ABC, abstractmethod


class Priced(ABC):
    @abstractmethod
    def price(self) -> int:
        ...


class Describable(ABC):
    @abstractmethod
    def describe(self) -> str:
        ...


class Subscription(Priced, Describable):
    pass


class MonthlySubscription(Subscription):
    def price(self):
        return 2000

    def describe(self):
        return "Месячный абонемент"


class YearlySubscription(Subscription):
    def price(self):
        return 18000

    def describe(self):
        return "Годовой абонемент"


class Client:
    def __init__(self, name):
        self.name = name
        self.subscription = None
        self.trainings = []


class Repository(ABC):
    @abstractmethod
    def add(self, client):
        ...


class ClientRepository(Repository):
    def __init__(self):
        self.clients = []

    def add(self, client):
        self.clients.append(client)


class FitnessService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def register(self, name):
        client = Client(name)
        self.repository.add(client)
        return client

    def issue(self, client, subscription: Subscription):
        client.subscription = subscription

    def sign_up(self, client, training):
        client.trainings.append(training)

    def cancel(self, client, training):
        if training in client.trainings:
            client.trainings.remove(training)


repo = ClientRepository()
service = FitnessService(repo)

client = service.register("Иван")
service.issue(client, MonthlySubscription())
service.sign_up(client, "йога")
service.sign_up(client, "бокс")
service.cancel(client, "бокс")

print("Клиент:", client.name)
print(client.subscription.describe(), "-", client.subscription.price(), "руб.")
print("Тренировки:", client.trainings)

for sub in [MonthlySubscription(), YearlySubscription()]:
    print(sub.describe(), "-", sub.price(), "руб.")
