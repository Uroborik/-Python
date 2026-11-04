from datetime import datetime, timedelta


def datetimes(x):
    start = datetime.today()
    return [start + timedelta(days=x * i) for i in range(20)]


result = datetimes(7)
print("Всего дат:", len(result))
for d in result:
    print(d)
