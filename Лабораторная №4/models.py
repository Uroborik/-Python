class Order:
    def __init__(self, number, client, items, status="новый"):
        self.number = number
        self.client = client
        self.items = items
        self.status = status

    def cost(self):
        return sum(price for _, price in self.items)

    def to_dict(self):
        return {"number": self.number, "client": self.client,
                "items": self.items, "status": self.status}

    @classmethod
    def from_dict(cls, d):
        return cls(d["number"], d["client"], d["items"], d["status"])

    def __str__(self):
        return f"№{self.number} | {self.client} | {self.cost()} руб. | {self.status}"
