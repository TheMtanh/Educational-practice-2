class Worker:
    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_rate(self):
        return self.__rate

    def get_days(self):
        return self.__days

    def get_salary(self):
        return self.__rate * self.__days

    def show_info(self):
        print(f"{self.__name} {self.__surname}.\n"
              f"Ставка: {self.__rate}, Дней: {self.__days}, Зарплата: {self.get_salary()}")


workers = [
    Worker("Иван", "Денисов", 358, 31),
    Worker("Евгений", "Понасенков", 230, 16),
    Worker("Иоанн", "Пресвитер", 1, 999)
]


def add_worker():
    name = input("Имя: ")
    surname = input("Фамилия: ")
    rate = int(input("Ставка за день: "))
    days = int(input("Количество рабочих дней: "))
    w = Worker(name, surname, rate, days)
    workers.append(w)
    print("Добавлен!\n")


def list_workers():
    if not workers:
        print("Никого нет")
    else:
        for i, w in enumerate(workers, 1):
            print(f"{i}. ", end="")
            w.show_info()
    print()


def menu():
    while True:
        print("Управление сотрудниками (0-0)\n")
        print("1. Показать работников")
        print("2. Добавить нового")
        print("0. Я ухожу")
        choice = input("\nУкажите действие: ")

        if choice == "1":
            list_workers()
        elif choice == "2":
            add_worker()
        elif choice == "0":
            print("Всего хорошего")
            break
        else:
            print("Вы ввели не то, попробуйте снова\n")


menu()
