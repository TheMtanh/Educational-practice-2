class Counter:
    def __init__(self, value=0):
        self.value = value

    def increase(self):
        self.value += 1

    def decrease(self):
        self.value -= 1

    def get_value(self):
        return self.value


def main():
    start = input("Введите начальное значение: ")
    if start.strip() == "":
        counter = Counter()
    else:
        try:
            counter = Counter(int(start))
        except ValueError:
            print("Ошибка ввода. Используется значение по умолчанию (0).")
            counter = Counter()

    while True:
        print("\nТекущее значение счётчика:", counter.get_value())
        print("Выберите действие")
        print("+ — Увеличить")
        print("- — Уменьшить")
        print("= — Выход")

        choice = input("Вы выбрали: ")

        if choice == "+":
            counter.increase()
        elif choice == "-":
            counter.decrease()
        elif choice == "=":
            print("Выход")
            break
        else:
            print("Неверный выбор. Попробуйте снова")


main()
