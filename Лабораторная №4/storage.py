import json
from models import Order


def save(orders, filename="data.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([o.to_dict() for o in orders], f, ensure_ascii=False, indent=2)


def load(filename="data.json"):
    try:
        with open(filename, encoding="utf-8") as f:
            return [Order.from_dict(d) for d in json.load(f)]
    except FileNotFoundError:
        return []
