class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print("Число a:", self.a)
        print("Число b:", self.b)

    def update(self, new_a, new_b):
        self.a = new_a
        self.b = new_b
        print("Значения обновлены")

    def get_sum(self):
        return self.a + self.b

    def get_max(self):
        return max(self.a, self.b)


def main():
    p = Pair(10, 20)

    print("Исходные значения:")
    p.show()

    print("\nСумма чисел:", p.get_sum())
    print("Наибольшее число:", p.get_max())

    print("\nИзменим значения")
    new_a = int(input("Введите a: "))
    new_b = int(input("Введите b: "))
    p.update(new_a, new_b)

    print("\nОбновлено: ")
    p.show()
    print("Сумма чисел: ", p.get_sum())
    print("Наибольшее число: ", p.get_max())


main()
