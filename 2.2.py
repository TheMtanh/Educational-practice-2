class Train:
    def __init__(self, train_number, destination, departure_time):
        self.train_number = train_number
        self.destination = destination
        self.departure_time = departure_time

    def info(self):
        print("Номер поезда:", self.train_number)
        print("Место назначения:", self.destination)
        print("Время отправления:", self.departure_time)


trains = [
    Train(78, "Нижний Новгород", "8:05"),
    Train(112, "Берёзово", "13:44"),
    Train(14, "Санкт-Петербург", "17:03"),
    Train(34, "Москва", "19:00")
]


def main():
    while True:
        print("\nСписок поездов на завтра:")
        for train in trains:
            print(f"Поезд №{train.train_number} -> {train.destination} ({train.departure_time})")

        cmd = input("Введите номер поезда для получения информации (или '0' для выхода): ")

        if cmd == "0":
            print("Выход из программы")
            break

        found = False
        for train in trains:
            if str(train.train_number) == cmd:
                print("\nИнформация о поезде: ")
                train.info()
                found = True
                break

        if not found:
            print("Поезд с таким номером не найден")


main()
