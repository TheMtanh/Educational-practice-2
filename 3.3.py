class Calculation:
    def __init__(self, calculationLine=""):
        self.calculationLine = calculationLine

    def SetCalculationLine(self, new_line):
        self.calculationLine = new_line

    def SetLastSymbolCalculationLine(self, symbol):
        self.calculationLine += symbol

    def GetCalculationLine(self):
        return self.calculationLine

    def GetLastSymbol(self):
        if self.calculationLine:
            return self.calculationLine[-1]
        return None

    def DeleteLastSymbol(self):
        if self.calculationLine:
            self.calculationLine = self.calculationLine[:-1]


def menu():
    calc = Calculation()

    while True:
        print("\n1. Установить строку")
        print("2. Добавить символ в конец")
        print("3. Показать текущую строку")
        print("4. Получить последний символ")
        print("5. Удалить последний символ")
        print("0. Выход")

        choice = input("\nВаше действие: ")

        if choice == "1":
            new_line = input("Введите новую строку: ")
            calc.SetCalculationLine(new_line)
            print("\nОбновлено")

        elif choice == "2":
            symbol = input("Введите символ: ")
            if symbol:
                calc.SetLastSymbolCalculationLine(symbol[0])
                print("Добавлено")

        elif choice == "3":
            print("Текущая строка:", calc.GetCalculationLine())

        elif choice == "4":
            last = calc.GetLastSymbol()
            if last:
                print("Последний символ:", last)
            else:
                print("Строка пуста")

        elif choice == "5":
            calc.DeleteLastSymbol()
            print("Символ удалён")
            print("Результат:", calc.GetCalculationLine())

        elif choice == "0":
            print("Выход")
            break

        else:
            print("Попробуйте ещё раз")


menu()
