class Example:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print(f"Создан объект; x = {self.x}, y = {self.y}")

    def __del__(self):
        print(f"Объект: x = {self.x}, y = {self.y} удалён")

    def show(self):
        print(f"Значения: x = {self.x}, y = {self.y}")


def main():
    obj = None

    while True:
        print("\nМеню")
        print("1 — Создать объект с заданными значениями")
        print("2 — Создать со значениями по умолчанию")
        print("3 — Показать значения")
        print("4 — Удалить")
        print("0 — Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            try:
                x = int(input("Введите значение x: "))
                y = int(input("Введите значение y: "))
                obj = Example(x, y)
            except ValueError:
                print("Ошибка ввода. Введите целые числа")
        elif choice == "2":
            obj = Example()
        elif choice == "3":
            if obj:
                obj.show()
            else:
                print("Объект не создан")
        elif choice == "4":
            if obj:
                del obj
                obj = None
            else:
                print("Объект отсутствует")
        elif choice == "0":
            print("Выход")
            break
        else:
            print("Неверный выбор. Попробуйте ещё раз")


main()
