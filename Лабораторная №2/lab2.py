
def main():
    shet = [
        {
            "number": "67",
            "name": "Lyuboe",
            "type": "Vklad",
            "balance": "148800"
        },
        {
            "number": "69",
            "name": "Kakoeto",
            "type": "Tekushiy",
            "balance": "520000"
        }
    ]
    while True:
        print('Выберете',
              '1 - поиск по владельцам',
              '2 - фильтрацию по типу',
              '3 - определение общего баланса',
              '4 - поиск счёта с максимальным балансом',
              '5 - список типов счетов',
              '6 - сортировку по балансу',
              '7 - выход', sep='\n')
        Menu = input()
        if Menu == '1':
            Udobnaya = input('Введите имя владельца: ')
            for i in shet :
                if i["name"] == Udobnaya:
                    print(f'Счет владельца {Udobnaya}: {i["number"]}')

        elif Menu == '2':
            Udobnaya = input('Введите тип счета: ')
            for i in shet:
                if i["type"] == Udobnaya:
                    print(f'Счета типа {Udobnaya}: {i["number"]}')

        elif Menu == '3':
            sum_ = 0
            for i in shet:
                sum_ += int(i["balance"])
            print(f'Сумма равна: {sum_}')

        elif Menu == '4':
            max_ = -1
            num = ''
            for i in shet:
                if max_ < int(i["balance"]):
                    max_ = int(i["balance"])
                    num = i["number"]
            print(f"Номер счета с наибольшим балансом ({max_}): {num}")

        elif Menu == '5':
            list_ = []
            for i in shet:
                Peremena = i['type']
                list_.append(Peremena)
            list_ = list(set(list_))
            print(f'Список типов счетов: {list_}')

        elif Menu == '6':
            list_ = []
            for i in shet:
                Zvonok = int(i["balance"])
                list_.append(Zvonok)
            list_ = sorted(list_)
            for i in list_:
                for j in shet:
                    if i == int(j["balance"]):
                        print(f'Счет №{j['number']} имеет баланс: {j["balance"]}')

        elif Menu == '7':
            break
        else:
            print('Введите число от 1 до 7')


if __name__ == '__main__':
    main()