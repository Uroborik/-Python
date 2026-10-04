from models import Order
from services import OrderService
from storage import save, load
from exceptions import OrderNotFoundError


def input_items():
    items = []
    n = int(input("Сколько товаров: "))
    for i in range(n):
        name = input(f"Товар {i + 1}: ")
        price = float(input("Цена: "))
        items.append([name, price])
    return items


def main():
    service = OrderService(load())
    while True:
        print("\n1-добавить 2-статус 3-поиск 4-отмена 5-список 0-выход")
        cmd = input("Выбор: ")
        try:
            if cmd == "1":
                number = int(input("Номер: "))
                client = input("Клиент: ")
                service.add(Order(number, client, input_items()))
            elif cmd == "2":
                number = int(input("Номер: "))
                service.set_status(number, input("Новый статус: "))
            elif cmd == "3":
                print(service.find(int(input("Номер: "))))
            elif cmd == "4":
                service.cancel(int(input("Номер: ")))
            elif cmd == "5":
                for o in service.orders:
                    print(o)
            elif cmd == "0":
                save(service.orders)
                break
        except OrderNotFoundError as e:
            print(e)
        except ValueError:
            print("Некорректный ввод")


if __name__ == "__main__":
    main()
