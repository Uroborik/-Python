def sum_training(training):
    sum_ = 0
    for i in training:
        sum_ += i
    return sum_


def max_training(training):
    max_ = -1.0
    number = 0

    for i in range(len(training)):
        if training[i] > max_:
            max_ = max(training[i], max_)
            number = i + 1

    return number, max_


def average(training):
    return sum_training(training) / len(training)


def more_than_hour(training):
    list_ = []

    for i in training:
        if i > 60:
            list_.append(i)

    return len(list_)


def less_than_30_percent(training):
    list_ = []

    for i in training:
        if i < 30:
            list_.append(i)

    return len(list_) / len(training) * 100


def main():
    while True:
        menu = int(input('1 - запуск, 0 - выход '))

        if menu == 0:
            break

        training = list()

        count = int(input('Введите количество тренировок: '))

        if count <= 0:
            print('Количество тренировок должно быть больше 0')
            continue

        for i in range(count):
            while True:
                training_time = float(
                    input(f'Введите продолжительность тренировки {i + 1}: ')
                )

                if training_time > 0:
                    break
                else:
                    print(
                        'Продолжительность тренировки должна быть больше 0'
                    )

            training.append(training_time)

        print('Суммарная продолжительность тренировок = ',
              sum_training(training))

        print('Средняя продолжительность тренировки = ',
              average(training))

        print('Самая длинная тренировка',
              max_training(training)[0],
              '(',
              max_training(training)[1],
              'мин.)')

        print('Количество тренировок продолжительностью более часа = ',
              more_than_hour(training))

        print('Процент тренировок продолжительностью менее 30 минут = ',
              less_than_30_percent(training),
              '%')


if __name__ == '__main__':
    main()